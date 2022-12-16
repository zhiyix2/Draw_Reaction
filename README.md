# Draw_Reaction




  

To setup the environment for executing "python Draw_Reaction.py" you need to install the Tkinter
You can execute "pip install tk" in the terminal
Run the program by executing "python Draw_Reaction.py <TXT File Path>"


[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]


## About The Project

This program draws reactions from a txt file with reactions in the SBML format.


### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

To setup the environment for executing "python Draw_Reaction.py" you need to install the Tkinter by typing "pip install tk" in the terminal
the program can be run by executing "python Draw_Reaction.py <TXT File Path>"



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

To setup the environment for executing "python Draw_Reaction.py" you need to install the Tkinter by typing "pip install tk" in the terminal


### Installation

There are two options to install the program.

1. Clone the repo from GitHub
  ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Install the package using pip
   ```sh
   npm install
   ```


## Usage



This program can be run by executing the following:
  ```sh
   python Draw_Reaction.py <TXT File Path>
  ```
This program draws reactions from given txt file.
The given txt file has to include the reaction section according to the format below:
// Reactions:
  ```sh
  J0: MKKK => MKKK_P; uVol*J0_V1*MKKK/((1 + (MAPK_PP/J0_Ki)^J0_n)*(J0_K1 + MKKK));

  J1: MKKK_P => MKKK; uVol*J1_V2*MKKK_P/(J1_KK2 + MKKK_P);

  J2: MKK => MKK_P; uVol*J2_k3*MKKK_P*MKK/(J2_KK3 + MKK);

  J3: MKK_P => MKK_PP; uVol*J3_k4*MKKK_P*MKK_P/(J3_KK4 + MKK_P);

  J4: MKK_PP => MKK_P; uVol*J4_V5*MKK_PP/(J4_KK5 + MKK_PP);

  J5: MKK_P => MKK; uVol*J5_V6*MKK_P/(J5_KK6 + MKK_P);
  ```


