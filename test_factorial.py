import pytest
from codeweaver.core.iterative_programmer import setup_agent, CodeResult

def test_factorial_basic():
    programmer = setup_agent()
    result = programmer.forward("Create a function that calculates factorial of a number")
    
    # Execute the generated code
    local_vars = {}
    exec(result.code, {}, local_vars)
    factorial = local_vars['factorial']
    
    # Test basic cases
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    
def test_factorial_negative():
    programmer = setup_agent()
    result = programmer.forward("Create a function that calculates factorial of a number")
    
    # Execute the generated code
    local_vars = {}
    exec(result.code, {}, local_vars)
    factorial = local_vars['factorial']
    
    # Test negative input
    with pytest.raises(ValueError):
        factorial(-1)

def test_code_result_structure():
    programmer = setup_agent()
    result = programmer.forward("Create a function that calculates factorial of a number")
    
    assert isinstance(result, CodeResult)
    assert isinstance(result.code, str)
    assert isinstance(result.success, bool)
    assert isinstance(result.output, str)
    assert result.success == True
    assert "factorial" in result.code