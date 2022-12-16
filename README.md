# Draw_Reaction
[![Latest Version](https://img.shields.io/pypi/v/tkshapes.svg)](https://pypi.org/project/tkshapes/)


## About The Project
![Draw Reaction](https://github.com/zhiyix2/Draw_Reaction/blob/main/Image/Demo.png)
This program draws reactions from a txt file with reactions in the SBML format.


<!-- GETTING STARTED -->
## Getting Started
The followings are the instructions on setting the program locally.

### Prerequisites
1. Python 3.10 or higher.
2. Tkinter 0.1.0 or higher.
To setup the environment for executing "python Draw_Reaction.py" you need to install the Tkinter by typing "pip install tk" in the terminal/cml.
  ```sh
   pip install tk
   ```


### Installation

There are two options to install the program.

1. Clone the repo from GitHub
  ```sh
   git clone https://github.com/zhiyix2/Draw_Reaction.git
   ```
2. Install the package using pip
  ```sh
   pip install Draw_Reaction-zhiyix2
  ```


## Usage

This program can be run by executing the following:
  ```sh
   python __main__.py <TXT File Path>
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



## License

Distributed under the MIT License. See `LICENSE` for more information.

[![MIT License](https://github.com/zhiyix2/Draw_Reaction/blob/main/Image/license.svg)](https://github.com/zhiyix2/Draw_Reaction/blob/main/LICENSE)


## Contact

Zhiying Xie - zhiyix2@uw.edu

Project Link: [https://github.com/zhiyix2/Draw_Reaction.git](https://github.com/zhiyix2/Draw_Reaction)




