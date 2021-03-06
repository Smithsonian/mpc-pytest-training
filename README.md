[![Unit Tests](https://github.com/Smithsonian/mpc-pytest-training/actions/workflows/mpc-pytest.yml/badge.svg)](https://github.com/Smithsonian/mpc-pytest-training/actions/workflows/mpc-pytest.yml)

# mpc-pytest-training
Repository used for interactive pytest training at the Minor Planet Center. Inside this repository is a simple Flask web application that displays the output from functions you all will implement (and test!). The concept is a random integer will be passed into a premade function with your name on it, and you implement code to do something to the number, and return the result. Below are the steps to follow for this training.

## Agenda
1. Create Github accounts, and get everyone added to this repository
2. (optional) [Set up github ssh keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
3. [Unit Test Lecture](https://docs.google.com/presentation/d/1_bCQLQ564H-benVRhXpQnSIA3Ko9JyoW/edit?usp=sharing&ouid=100235637949753397026&rtpof=true&sd=true)
4. Interactive pytest exercise (using this repo)
5. Work together to create a test for some operational code

## Setup
1. Clone the repository

   `git clone https://github.com/Smithsonian/mpc-pytest-training.git`
     
   or if you have ssh keys set up: 

   `git clone git@github.com:Smithsonian/mpc-pytest-training.git`
2. Go into the new repo 

   `cd mpc-pytest-training`
3. Create a branch and switch to it 
  
   `git checkout -b name_of_branch` 
4. Install the mpc_training package (with the -e edit flag) 

   `pip install -e .` 
5. Run pytest and ensure the tests pass

    `pytest` 
6. Go to the `flask_app` directory and run flask. Check that the website shows up
   ```
   cd flask_app
   flask run
   ```
   view at `http://127.0.0.1:5000/`

## Exercise
1. Open the mpc_training/team.py file, and find the function with your name on it.
2. Pick your favorite mathematical operation (see Chris' sqrt example), but don't implement it quite yet. Just put a comment in the function to convey your goal. We will come back here once we write a test.
3. Create a new python file in the tests directory called "test_yourname.py", feel free to copy and rename test_chris.py. Remember - pytest automatically finds files prefixed with "test_".
4. Write a test to check your function's output, and run it to ensure it fails :)
5. Now go back to mpc_training/team.py and implement your function, and re-run your unit test until it passes.
6. Now test your function manually by restarting flask ("ctrl-c", "flask run"), and refreshing the localhost page which should still be up in your browser. Make sure you see your output, and you are happy with it.  
7. Add new files to git, Commit and Push your code

   ```
   git add .
   git commit -m "Implemented function for your_name, and also a correponding unit test"
   git push --set-upstream origin
   ```
9. Check if your branch passes the tests running in [Github Actions](https://github.com/Smithsonian/mpc-pytest-training/actions) 
10. Open a [new pull request](https://github.com/Smithsonian/mpc-pytest-training/pulls) for your branch by clicking the green "New Pull Request" button
11. You are done!  Chris and N will be reviewing the pull requests and merging them.
