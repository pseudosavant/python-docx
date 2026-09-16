"""Acceptance steps for hyperlink authoring."""

from io import BytesIO

from behave import given, then, when
from behave.runner import Context

from docx import Document
from docx.enum.style import WD_STYLE_TYPE

from helpers import test_docx, test_file


@given("an existing hyperlink for authoring")
def given_an_existing_hyperlink_for_authoring(context: Context):
    context.document = Document(test_docx("par-hyperlinks"))
    context.document.styles.add_style("Link emphasis", WD_STYLE_TYPE.CHARACTER)
    context.hyperlink = context.document.paragraphs[1].hyperlinks[0]
    context.original_text = context.hyperlink.text
    context.original_run_count = len(context.hyperlink.runs)


@when("I append formatted runs to the hyperlink")
def when_I_append_formatted_runs_to_the_hyperlink(context: Context):
    context.hyperlink.add_run(" Café\t").bold = True
    context.hyperlink.add_run("code\n", "Link emphasis").font.name = "Consolas"


@then("the appended runs retain their text and formatting after saving")
def then_the_appended_runs_retain_their_text_and_formatting(context: Context):
    stream = BytesIO()
    context.document.save(stream)
    hyperlink = Document(stream).paragraphs[1].hyperlinks[0]
    assert hyperlink.text == context.original_text + " Café\tcode\n"
    assert hyperlink.runs[-2].bold is True
    assert hyperlink.runs[-1].style.name == "Link emphasis"
    assert hyperlink.runs[-1].font.name == "Consolas"


@when("I append a picture run to the hyperlink")
def when_I_append_a_picture_run_to_the_hyperlink(context: Context):
    context.picture = context.hyperlink.add_run().add_picture(test_file("python-icon.jpeg"))


@then("the hyperlink contains the picture after saving")
def then_the_hyperlink_contains_the_picture_after_saving(context: Context):
    stream = BytesIO()
    context.document.save(stream)
    hyperlink = Document(stream).paragraphs[1].hyperlinks[0]
    assert hyperlink.text == context.original_text
    assert len(hyperlink.runs) == context.original_run_count + 1
    assert len(list(hyperlink.runs[-1].iter_inner_content())) == 1
    assert context.picture.width > 0


@when("I try to append a run with a missing character style")
def when_I_try_to_append_a_run_with_a_missing_character_style(context: Context):
    try:
        context.hyperlink.add_run("label", "Missing hyperlink style")
    except KeyError:
        return
    raise AssertionError("Expected a KeyError for the missing style")


@then("the hyperlink's runs remain unchanged")
def then_the_hyperlinks_runs_remain_unchanged(context: Context):
    assert context.hyperlink.text == context.original_text
    assert len(context.hyperlink.runs) == context.original_run_count
