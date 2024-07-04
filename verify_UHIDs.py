import pandas as pd
import os

def verify_uhids(path_to_csv):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(path_to_csv)
    
    # Assuming 'Patient ID (UHID)' is the column name in your CSV
    patient_uhids = df['Patient ID (UHID)'].tolist()
    
    # Initialize an empty array to store UHIDs with paths found
    uhids_with_paths = []
    
    # Iterate over each UHID
    for uhid in patient_uhids:
        # Construct the terminal command
        command = f'find . -type d -name "{uhid}"'
        
        # Execute the command using os.system and capture the output
        result = os.popen(command).read().strip()
        
        # Check if result is not empty (i.e., path found)
        if result:
            uhids_with_paths.append((uhid, result))
    
    # Print the array containing UHIDs with paths found
    print(uhids_with_paths)



'''
100008174   105073332  105323125  105340988  105361383    500223418  500261581  500262283  500262622  500262907  500263193  500263489  500263793  500264298  500264700  500265012  500265855  500276699
100013247   105109969  105324598  105341041  105362702    500238387  500261582  500262286  500262629  500262909  500263196  500263492  500263813  500264299  500264707  500265013  500265858  500276707
100055644   105124081  105324611  105341976  105362852    500255556  500261589  500262296  500262632  500262913  500263199  500263502  500263830  500264300  500264710  500265014  500265862  500276776
100329610   105130163  105325079  105342256  105362972    500258924  500261593  500262297  500262634  500262919  500263202  500263504  500263842  500264319  500264713  500265101  500265873  500276778
100461543   105133072  105325104  105342289  105363041    500260813  500261601  500262305  500262636  500262925  500263203  500263505  500263843  500264322  500264719  500265319  500265885  500276801
100477519   105168538  105325456  105342389  105365290    500260819  500261606  500262306  500262640  500262927  500263205  500263506  500263845  500264330  500264732  500265364  500265886  500276805
100535511   105170545  105325512  105342693  105365850    500261024  500261624  500262307  500262641  500262933  500263215  500263507  500263848  500264331  500264735  500265387  500265889  500276811
100643712   105189077  105325623  105342885  105367668    500261148  500261625  500262316  500262648  500262935  500263221  500263508  500263850  500264343  500264740  500265495  500265890  500282871
100724288   105202346  105325641  105343123  105369245    500261258  500261659  500262321  500262649  500262937  500263224  500263512  500263852  500264350  500264745  500265569  500265895  500283378
100921875   105202386  105325690  105343420  105370072    500261378  500261683  500262334  500262650  500262945  500263233  500263513  500263860  500264351  500264748  500265591  500265902  500283469
101075443   105217546  105326325  105343538  105370480    500261388  500261688  500262340  500262653  500262950  500263234  500263519  500263861  500264354  500264752  500265607  500265904  500283565
101123383   105222403  105326508  105344080  105370868    500261396  500261700  500262343  500262658  500262951  500263236  500263522  500263868  500264356  500264754  500265610  500265914  500283569
101150678   105227763  105326550  105344146  105370884    500261408  500261706  500262344  500262659  500262953  500263238  500263524  500263870  500264357  500264755  500265611  500265915  500283570
101169894   105234778  105326589  105344471  105370894    500261409  500261720  500262350  500262663  500262960  500263241  500263525  500263883  500264358  500264762  500265615  500265922  500283571
101206047   105242989  105327994  105344799  105371050    500261422  500261731  500262359  500262668  500262963  500263253  500263526  500263887  500264364  500264774  500265621  500265925  500283585
101278047   105255806  105328170  105345763  105371070    500261430  500261741  500262365  500262670  500262965  500263254  500263538  500263892  500264368  500264776  500265625  500265935  500283586
101453181   105266751  105328319  105346047  105372560    500261436  500261748  500262366  500262671  500262966  500263255  500263539  500263902  500264379  500264778  500265640  500265943  500283587
101536955   105268689  105328344  105346346  105372586    500261437  500261758  500262373  500262673  500262968  500263263  500263544  500263903  500264395  500264780  500265643  500265945  500283588
101769301   105269126  105328648  105347244  105374376    500261447  500261780  500262376  500262691  500262969  500263264  500263548  500263904  500264435  500264782  500265651  500265951  500283600
101790180   105269774  105328781  105347282  105374416    500261449  500261787  500262378  500262692  500262970  500263275  500263551  500263915  500264447  500264784  500265654  500265955  500283605
102018938   105269943  105328798  105347286  105374704    500261456  500261788  500262379  500262693  500262972  500263280  500263562  500263919  500264451  500264788  500265665  500265958  500283618
102214326   105270394  105328804  105347398  105375302    500261469  500261790  500262381  500262695  500262976  500263286  500263572  500263923  500264455  500264800  500265667  500265959  500283626
102547145   105272160  105329343  105347445  105375505    500261471  500261812  500262382  500262699  500262985  500263305  500263578  500263925  500264461  500264802  500265674  500265960  500283632
102622525   105274439  105329387  105347478  105375536    500261472  500261821  500262383  500262703  500262995  500263315  500263579  500263934  500264473  500264803  500265679  500265961  500283635
102659801   105278488  105329580  105347557  105375578    500261476  500261834  500262388  500262709  500262996  500263317  500263584  500263935  500264475  500264805  500265682  500265964  500283640
102743796   105279859  105330176  105347575  105375631    500261477  500261837  500262398  500262710  500262998  500263324  500263594  500263936  500264480  500264808  500265683  500265965  500283651
102794413   105281725  105330613  105347590  105375737    500261486  500261845  500262401  500262711  500263000  500263325  500263595  500263940  500264481  500264812  500265692  500265969  500283661
102837884   105281780  105330884  105348645  105376697    500261488  500261847  500262407  500262714  500263003  500263330  500263597  500263947  500264484  500264814  500265695  500265975  500283663
102882261   105285091  105331000  105348655  105376960    500261489  500261848  500262408  500262715  500263011  500263337  500263598  500263950  500264488  500264817  500265698  500265979  500283671
103018656   105288114  105331114  105348970  105377005    500261492  500261862  500262417  500262716  500263044  500263341  500263603  500264061  500264501  500264823  500265702  500265989  500283684
103120468   105289919  105331606  105349031  105379028    500261498  500261866  500262418  500262723  500263059  500263344  500263606  500264094  500264506  500264825  500265709  500265990  500283688
103211282   105292233  105331953  105349075  105441083    500261502  500261918  500262422  500262725  500263078  500263346  500263607  500264097  500264511  500264829  500265719  500265993  500283694
103244914   105293072  105332907  105349368  105447375    500261503  500261947  500262429  500262726  500263090  500263347  500263609  500264105  500264536  500264838  500265740  500265998  500283726
103268707   105293826  105332975  105349811  105453840    500261504  500261969  500262430  500262728  500263091  500263355  500263613  500264106  500264553  500264839  500265745  500266000  500283746
103390636   105294890  105333012  105350514  105453954    500261506  500261972  500262432  500262745  500263094  500263362  500263618  500264113  500264558  500264849  500265749  500266007  500283752
103395364   105297851  105333081  105350547  105482904    500261508  500261985  500262436  500262749  500263095  500263370  500263623  500264114  500264559  500264873  500265750  500266008  500283767
103397221   105298348  105333131  105350605  105492844    500261509  500262040  500262437  500262753  500263098  500263372  500263625  500264115  500264574  500264878  500265753  500266010  500283774
103465030   105300161  105333247  105351581  105493510    500261512  500262102  500262443  500262755  500263114  500263377  500263626  500264116  500264576  500264882  500265756  500266011  500283778
103491795   105300424  105333252  105351622  105538943    500261513  500262116  500262450  500262759  500263117  500263381  500263631  500264117  500264577  500264887  500265757  500266012  500283780
1035633784  105300461  105333464  105351632  105544557    500261514  500262132  500262454  500262779  500263119  500263383  500263634  500264119  500264579  500264889  500265759  500266015  500283786
103851675   105301889  105334178  105351689  105545786    500261515  500262139  500262478  500262784  500263125  500263393  500263643  500264123  500264580  500264908  500265772  500266035  500283974
103868521   105302132  105334844  105351693  105545823    500261516  500262157  500262498  500262789  500263128  500263398  500263645  500264135  500264581  500264909  500265777  500266050  500284027
103974378   105304504  105335014  105351708  105546700    500261517  500262161  500262505  500262793  500263129  500263400  500263646  500264180  500264585  500264912  500265779  500266055  500285877
104043080   105306661  105335648  105351766  105552468    500261518  500262169  500262508  500262795  500263133  500263416  500263648  500264195  500264590  500264913  500265786  500266069  520257
104105421   105309013  105335776  105351803  20120569379  500261519  500262174  500262527  500262798  500263134  500263423  500263650  500264203  500264593  500264922  500265789  500266078
104109183   105311667  105335967  105352009  20130114899  500261520  500262201  500262535  500262800  500263138  500263424  500263651  500264204  500264595  500264936  500265794  500266080
104181642   105313108  105336027  105352062  20130155198  500261522  500262211  500262556  500262805  500263144  500263426  500263718  500264214  500264606  500264940  500265802  500266084
104332633   105313384  105337192  105352637  20130244418  500261525  500262214  500262558  500262812  500263153  500263432  500263727  500264219  500264611  500264942  500265803  500266086
104521941   105313701  105337264  105352711  20130319035  500261527  500262223  500262560  500262817  500263154  500263435  500263732  500264221  500264617  500264944  500265806  500266090
104531795   105314116  105337481  105353945  20130341354  500261529  500262243  500262562  500262818  500263157  500263438  500263741  500264235  500264659  500264946  500265810  500266091
104535721   105316190  105338901  105353962  20130451589  500261554  500262254  500262564  500262819  500263159  500263445  500263743  500264236  500264663  500264954  500265812  500266099
104557953   105316493  105339080  105355422  20130685318  500261555  500262255  500262572  500262822  500263161  500263446  500263744  500264261  500264665  500264957  500265820  500266100
104570487   105318079  105339124  105355528  20130713620  500261557  500262258  500262573  500262825  500263167  500263448  500263745  500264274  500264666  500264962  500265824  500266104
104796936   105319705  105339273  105355781  500120928    500261562  500262260  500262579  500262831  500263169  500263449  500263746  500264283  500264673  500264964  500265825  500266215
104831478   105320112  105339447  105356825  500121708    500261563  500262263  500262581  500262832  500263170  500263451  500263747  500264284  500264675  500264972  500265826  500266216
104884441   105320129  105339506  105356826  500156027    500261564  500262264  500262585  500262836  500263175  500263472  500263750  500264288  500264681  500264973  500265831  500266219
104891824   10532105   105339688  105359683  500200033    500261571  500262267  500262597  500262837  500263185  500263475  500263751  500264289  500264688  500264976  500265840  500266220
104982287   105321331  105340220  105359812  500204157    500261574  500262268  500262605  500262849  500263187  500263480  500263753  500264292  500264689  500264984  500265842  500266225
105014632   105321778  105340321  105359815  500206888    500261575  500262272  500262606  500262863  500263189  500263485  500263756  500264293  500264693  500264990  500265849  500266231
105043286   105321992  105340748  105360870  500208054    500261576  500262276  500262607  500262878  500263190  500263486  500263783  500264294  500264695  500265000  500265850  500267220
105067873   105323106  105340798  105360991  500216348    500261578  500262277  500262616  500262898  500263191  500263487  500263784  500264297  500264699  500265005  500265854  500276685


'''