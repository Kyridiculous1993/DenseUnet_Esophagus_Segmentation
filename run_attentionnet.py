from functions.call_attention_net import dense_classify
import numpy as np
import tensorflow as tf

# tf.disable_v2_behavior()
import os
#Training only on the second dataset
fold=0
np.random.seed(1)
tf.set_random_seed(1)

Logs= 'Log_2019_09_23/large_receptivefield/'
server_path='/exports/lkeb-hpc/syousefi/2-lkeb-17-dl01/syousefi/TestCode/EsophagusProject/Code/'
mixed_precision=True
# if mixed_precision ==True:
    # os.environ['TF_ENABLE_AUTO_MIXED_PRECISION'] = '1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

GPU= tf.test.is_gpu_available(
    cuda_only=False,
    min_cuda_compute_capability=None
)

# if GPU is False:
#     print('Check: no GPU available! ')
#     exit(1)

dc12=dense_classify( data=2,
                     # densnet_unet_config=[1,3,5,3,1],
                     densnet_unet_config=[1,3,5,3,1],
                     compression_coefficient=.75,
                     sample_no=2000000,
                     validation_samples=1980,
                     no_sample_per_each_itr=1000,
                     train_tag='',
                     validation_tag='',
                     test_tag='',
                     img_name='',label_name='', torso_tag='',
                     log_tag='-cross-noRand-train1-'+str(fold),
                     tumor_percent=.75,
                     other_percent=.25,
                     Logs=Logs,
                     fold=fold,
                     server_path=server_path,growth_rate=4)
#6 th was the first
dc12.run_net()


