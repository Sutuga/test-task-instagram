# Test Task

---

### Requirements

1. Git
2. Python >= 3.8
3. Pipenv = *

> [!TIP]
> You can also see all requirements in the Pipfile.

### Installation Windows (Not tested on other OS systems)
* Create working directory for the project
* Clone repository to the working directory
* Install pipenv
  ```
  pip install --user pipenv
  ```

    > [!IMPORTANT]
    > Make sure that %USERPROFILE%\AppData\Roaming\Python\Python3X\Scripts\ in the path environment variable.
    > If not, add manually. Check pipenv correctly installed by ```pipenv -h```
    
* Go to the cloned repo in the working directory
* Install project dependencies
    ```
    pipenv sync --dev
    ```
    > [!TIP]
    > Or you can use ```pipenv install``` to re-lock your dependencies

### Run tests

```
pipenv run pytest tests\test_home_task.py -v
```

### Caveats
The tests did not anticipate additional authorization or approval dialogs during the Instagram login process.
A new Instagram user account was created specifically for testing purposes.
Therefore, there is a possibility that Instagram may present additional screens or require an authorization step for the new account.
Please ensure you can log in to the user account without encountering any additional steps.