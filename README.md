# Statistically Comparing Scheduling Algorithms For Computer Networks


Description of Files Used:

1. pages.py: contains code for both the original page replacement policy, as well as min funding revocation algorithm
2. convert.py: contains the code to create modified csv files from the original csv file which contained several empty entries for the packets received
3. perswitch_perinterface_aggre_stats.csv: the raw csv file used for the said experiment which was converted into usable format using pages.py
4. temp.csv: final csv file used in pages.py for experiments.

<h3>Observation:</h3>
  <hr>
  
  These are the three graphs we get after we execute our code. 
  
  ![image](https://user-images.githubusercontent.com/99542174/169899171-de5e3328-9247-4399-811d-f8e3301a3cf0.png)

  
  The graph on the left is of the Min Funding Revocation Algorithm, whereas the one in the middle is of the plain oldest removal. The one on the right is the scenario where we do not consider any dropping of the switches once a certain limit is reaches.

  
  Please note that original replacement policy (of removing the oldest switch irrespective of data transferred) has packet sizes in the domain of 1e7; whereas the replacement policy used by Min-Funding Revocation Algorithm is of the order of magnitude 1e9, which is huge compared to the former, and also closer to the "accurate" value of 1e10 that we get once we consider all switches are kept on with no polling and switching off of them.
  
