# SSH
_SSH_ (_SpreadSHeet_) is an API for handling a basic spreadsheet. The spreadsheet follows _Excel_'s conventions. The spreadsheet implements three operations: _set_, _get_, and _evaluate_. The _set_ and _get_ operations assign and return the value of a cell, respectively. The _evaluate_ operation takes the content of a cell and returns the result of its evaluation (e.g., a cell containing "=1+1" evaluates to 2). 

You do not need to know more so far. The _User Stories_ section will provide further details.

## Instructions for You
* FORK this project and make sure your forked repository is PUBLIC. Then, IMPORT the forked project into PyCharm.
* You are asked to develop _SSH_ by following TDD with the support of **GAI4-TDD**.
* You DO NOT need to develop a GUI.
* You CANNOT change the signature of the provided methods, move the provided methods to other classes, or change the name of the provided classes. However, you CAN add fields, methods (e.g., methods called by the provided methods), or even classes (including other test classes), as long as you comply with the provided API.
* You CAN use the internet to consult Python APIs or QA sites (e.g., StackOverflow).
* You CANNOT use AI tools except for GAI4-TDD.
* You CANNOT interact with your colleagues. Work alone and do your best!
* The _SSH_ requirements are divided into a set of USER STORIES, which serve as a to-do list (see the _User Stories_ section).
* You should be able to incrementally develop _SSH_ without an upfront comprehension of all its requirements. DO NOT read ahead and handle the requirements (specified in the user stories) one at a time in the provided order. Develop _SSH_ by starting from the first story's requirement. When a story is IMPLEMENTED, move on to the NEXT one. A story is implemented when you are confident that your program correctly implements the functionality stipulated by the story's requirement. This implies that all your test cases for that story and all the test cases for the previous stories pass. You may need to review your program as you progress toward more advanced requirements.
* Each time you end a GREEN or REFACTOR phase, COMMIT.
* At the end of the task, PUSH your forked project and fill in the following post-questionnaire: https://forms.gle/USTwKAGVbYFv4gfu7.

## API Usage
Take some minutes to understand, in broad terms, how the API works. If you do not fully understand the API, do not worry because more details will be given later in the _User Stories_ section. A typical API usage follows.

```python
# Initialize an empty spreadsheet.
spreadsheet = SpreadSheet()
# Set two cells.
spreadsheet.set("A1", "=B1")
spreadsheet.set("B1", "42")
# Get the value of a given cell (e.g., the value of "A1" is "=B1").
value = spreadsheet.get("A1")
# Evaluate a given cell (e.g., the evaluation of "A1" is "42").
result = spreadsheet.evaluate("A1")
```

See the provided source files to improve your understanding of the API before starting to implement the user stories. 

## User Stories
Remember to read and implement the user stories once at a time (in the provided order). Therefore, do not read the next user story, if the current one is not implemented yet.

### User Story 1 -- Integer Numbers
The spreadsheet should handle correctly formatted integer numbers both signed and unsigned, so that when a cell containing an integer number is evaluated, the result of this evaluation is the number itself. When a number does not follow the integer format (e.g., it contains a decimal point, special symbols, characters, etc.), the result of this evaluation is the string "#Error".

**Requirement:**
* Implement `SpreadSheet.evaluate(self, cell: str) -> int | str` to evaluate the content of a cell containing an integer number.

**Examples:**
* If the cell "A1" contains "1", the result of its evaluation is 1.
* If the cell "A1" contains "1.5", the result of its evaluation is "#Error".

### User Story 2 -- Strings
The spreadsheet should handle strings entered between single quotes. When a cell containing a string is evaluated, the result of this evaluation is the string itself without quotes. When a string does not have heading or trailing quotes, the result of this evaluation is the string "#Error".

**Requirement:**
* Implement `SpreadSheet.evaluate(self, cell: str) -> int | str` to evaluate the content of a cell containing a string.

**Examples:**
* If the cell "A1" contains "'Apple'", the result of its evaluation is "Apple".
* If the cell "A1" contains "'Apple", the result of its evaluation is "#Error".

### User Story 3 -- Simple Formulas
The spreadsheet evaluates simple formulas (i.e., formulas without operators or cell references). A simple formula starts with the equal sign (=) followed by a string or integer number, and the evaluation of that cell returns the corresponding string or integer. When a cell contains an equal sign followed by a wrong string or integer number, the evaluation of that cell returns the string "#Error".

**Requirement:**
* Implement `SpreadSheet.evaluate(self, cell: str) -> int | str` to evaluate the content of a cell containing a simple formula.

**Examples:**
* If the cell "A1" contains "='Apple'", the result of its evaluation is "Apple".
* If the cell "A1" contains "=1", the result of its evaluation is 1.
* If the cell "A1" contains "='Apple", the result of its evaluation is "#Error".

### User Story 4 -- Simple Formulas with References
A formula can contain a reference to a cell, following Excel's convention (e.g., "A5"). In such a case, the evaluation is recursive, namely: the referenced cell is evaluated and the result of this evaluation is returned by the formula. When the value contained in a cell referenced by a formula is incorrect, the evaluation returns the string "#Error". There could be cases in which the formula contains circular references (e.g., "A5" contains a formula referencing "A1", and "A1" contains a formula referencing "A5"). In this case, the evaluation returns the string "#Circular".

**Requirement:**
* Implement `SpreadSheet.evaluate(self, cell: str) -> int | str` to evaluate the content of a cell containing a simple formula with a reference to a cell.

**Examples:**
* If the cell "A1" contains "=B1" and "B1" contains "42", the result of the evaluation of "A1" is 42.
* If the cell "A1" contains "=B1" and "B1" contains "42.5", the result of the evaluation of "A1" is "#Error".
* If the cell "A1" contains "=B1" and "B1" contains "=A1", the result of the evaluation of "A1" is "#Circular".

### User Story 5 -- Formulas with Arithmetic Operators
The spreadsheet performs integer addition, subtraction, multiplication, division, and module operations when the corresponding operators (i.e., +, -, *, /, and %) are present in a formula. Note that complex formulas take into account operator precedence (e.g., multiplications are evaluated before additions). When an operation cannot be performed because (1) the operators are incorrect integer numbers or (2) there is a division by zero, the evaluation returns the string "#Error".

**Requirement:**
* Implement `SpreadSheet.evaluate(self, cell: str) -> int | str` to evaluate the content of a cell containing a formula with arithmetic operators.

**Examples:**
* If the cell "A1" contains "=1+3", the result of its evaluation is 4.
* If the cell "A1" contains "=1+3.5", the result of its evaluation is "#Error".
* If the cell "A1" contains "=1/0", the result of its evaluation is "#Error".
* If the cell "A1" contains "=1+3*2", the result of its evaluation is 7.

### User Story 6 -- Formulas with Arithmetic Operators and References
A formula can contain both arithmetic operators and references to other cells. In such a case, the evaluation is recursive, namely: the referenced cells are evaluated and the results of these evaluations are used by the formula.
Note that there could be cases in which (1) the value contained in a cell referenced by a formula is incorrect (in this case, the evaluation returns the string "#Error") or (2) the formula contains circular references (in this case, the evaluation returns the string "#Circular").

**Requirement:**
* Implement `SpreadSheet.evaluate(self, cell: str) -> int | str` to evaluate the content of a cell containing a formula with arithmetic operators and references.

**Examples:**
* If the cell "A1" contains "=1+B1" and the cell "B1" contains "3", the result of the evaluation of "A1" is 4.
* If the cell "A1" contains "=1+B1" and the cell "B1" contains "3.1", the result of the evaluation of "A1" is "#Error".
* If the cell "A1" contains "=1+B1" and the cell "B1" contains "=A1", the result of the evaluation of "A1" is "#Circular".

### User Story 7 -- Formulas with String Concatenations
The spreadsheet performs string concatenations when the concatenation operator (&) is present in a formula. A string concatenation cannot be performed when the strings are wrongly formatted. In this case, the evaluation returns the string "#Error".

**Requirement:**
* Implement `SpreadSheet.evaluate(self, cell: str) -> int | str` to evaluate the content of a cell containing a formula with string concatenations.

**Examples:**
* If the cell "A1" contains "='Hello'&' World'", the result of its evaluation is "Hello World".
* If the cell "A1" contains "='Hello'&' World", the result of its evaluation is "#Error".

### User Story 8 -- Formulas with String Concatenations and References
A formula can contain both string concatenations and references to other cells. In such a case, the evaluation is recursive, namely: the referenced cells are evaluated and the results of these evaluations are used by the formula.
Note that there could be cases in which (1) the value contained in a cell referenced by a formula is incorrect (in this case, the evaluation returns the string "#Error") or (2) the formula contains circular references (in this case, the evaluation returns the string "#Circular").

**Requirement:**
* Implement `SpreadSheet.evaluate(self, cell: str) -> int | str` to evaluate the content of a cell containing a formula with string concatenations and references.

**Example:**
* If the cell "A1" contains "='Hello'&B1" and the cell "B1" contains "' World'", the result of the evaluation of "A1" is "Hello World".
* If the cell "A1" contains "='Hello'&B1" and the cell "B1" contains " World'", the result of the evaluation of "A1" is "#Error".
* If the cell "A1" contains "='Hello'&B1" and the cell "B1" contains "=A1", the result of the evaluation of "A1" is "#Circular".

### User Story 9 -- Formulas with Parentheses
A formula can contain parentheses. When this happens, the part within the parentheses is evaluated first. If the parentheses in a formula are unbalanced, it returns the string "#Error". Note that a formula can contain arbitrary whitespaces, which are ignored.

**Requirement:**
* Implement `SpreadSheet.evaluate(self, cell: str) -> int | str` to evaluate the content of a cell containing a formula with parentheses.

**Examples:**
* If the cell "A1" contains "=2*(1+2)", the result of this evaluation is 6.
* If the cell "A1" contains "= 2 * (1 + 2)", the result of this evaluation is 6.

### User Story 10 -- Formulas with Parentheses and References
A formula can contain parentheses and references. In such a case, the evaluation is recursive, namely: the referenced cells are evaluated and the results of these evaluations are used by the formula.
Note that there could be cases in which (1) the value contained in a cell referenced by a formula is incorrect (in this case, the evaluation returns the string "#Error") or (2) the formula contains circular references (in this case, the evaluation returns the string "#Circular"). Moreover, a formula can contain arbitrary whitespaces, which are ignored.

**Requirement:**
* Implement `SpreadSheet.evaluate(self, cell: str) -> int | str` to evaluate the content of a cell containing a formula with parentheses and references. 

**Examples:**
* If the cell "A1" contains "=2*(1+B1)" and the cell "B1" contains "2", the result of this evaluation is 6.
* If the cell "A1" contains "= 2 * (1 + B1)" and the cell "B1" contains "2", the result of this evaluation is 6.
* If the cell "A1" contains "=2*(1+B1)" and the cell "B1" contains "2.1", the result of this evaluation is "#Error".
* If the cell "A1" contains "=2*(1+B1)" and the cell "B1" contains "=A1", the result of this evaluation is "#Circular".
