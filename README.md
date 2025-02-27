The goals of this Project are 

1. To implement partially an optimization procedure presented in the
paper: _Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks_. 
By partially I mean implementation is not one-to-one to the optimization procedure. 

2. Run this project completely on google colab

The purpose of this is to lear how one can use Keras custom training loops. 
Under keras custom training loop I mean, defining own loss function, and own layers.

The dataset and model are taken from Bolun Wang's [Repository](https://github.com/bolunwang/backdoor). 
The code is partially based on Bolun Wang's implementation as well.

Possible output after running `generate_trigger.ipynb`:

<p align="center">
  <img src="./images/traffic_sign.JPG" width="150" />
  <img src="./images/trigger.JPG" width="150" /> 
  <img src="./images/triggered.JPG" width="150" />
</p>

So, all traffic signs are going be with high probability classified as class 33
if the trigger is added. Remark that there are in total 43 classes.

To clone and set this repo on google colab I followed [Vortana Say](https://towardsdatascience.com/google-drive-google-colab-github-dont-just-read-do-it-5554d5824228)'s article.
However, to push commited changes back to repo I followed [Navaneeth Kt](https://medium.com/@navan0/how-to-push-files-into-github-from-google-colab-379fd0077aa8)'s article.