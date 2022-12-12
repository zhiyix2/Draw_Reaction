# Draw_Reaction

This program draws reactions from given txt file.
It draws reactions from the format:
// Reactions:
  J0: MKKK => MKKK_P; uVol*J0_V1*MKKK/((1 + (MAPK_PP/J0_Ki)^J0_n)*(J0_K1 + MKKK));
  J1: MKKK_P => MKKK; uVol*J1_V2*MKKK_P/(J1_KK2 + MKKK_P);
  J2: MKK => MKK_P; uVol*J2_k3*MKKK_P*MKK/(J2_KK3 + MKK);
  J3: MKK_P => MKK_PP; uVol*J3_k4*MKKK_P*MKK_P/(J3_KK4 + MKK_P);
  J4: MKK_PP => MKK_P; uVol*J4_V5*MKK_PP/(J4_KK5 + MKK_PP);
  J5: MKK_P => MKK; uVol*J5_V6*MKK_P/(J5_KK6 + MKK_P);
  J6: MAPK => MAPK_P; uVol*J6_k7*MKK_PP*MAPK/(J6_KK7 + MAPK);
  J7: MAPK_P => MAPK_PP; uVol*J7_k8*MKK_PP*MAPK_P/(J7_KK8 + MAPK_P);
  J8: MAPK_PP => MAPK_P; uVol*J8_V9*MAPK_PP/(J8_KK9 + MAPK_PP);
  J9: MAPK_P => MAPK; uVol*J9_V10*MAPK_P/(J9_KK10 + MAPK_P);

To setup the environment for executing "python Draw_Reaction.py" you need to install the Tkinter
You can execute "pip install tk" in the terminal
Run the program by executing "python Draw_Reaction.py <TXT File Path>"