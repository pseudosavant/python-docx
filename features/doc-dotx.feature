Feature: Instantiate documents from macro-free Word templates
  Scenario: Save a real document from a DOTX template
    Given a Word-authored DOTX template with styles and content
     When I instantiate a document from that template and save it
     Then the saved package is a DOCX and retains its template content
