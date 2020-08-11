# Re-evaluating Knowledge Graph Embedding Models on Domain Specific Datasets:

This experiment aims to answer the question on whether KGE models perform differently on domain specific datasets compared to generic ones like Freebase and Wordnet, which are commonly used in ML benchmarks.

I conducted the experiment using the [LibKGE](https://github.com/uma-pi1/kge) framework. This project includes the data dumps used for AIFB and MUTAG, the CSV files with all trials as well as the the best model configurations yaml files.

I used  two  domain  specific  datasets  (AIFB and  MUTAG),  both  bound  by  strong  ontological  information.  The experiment aims to  explain how hyperparameters affect KGE model performance on domain specific datasets by searching across a large hyperparameter space and then evaluating performance us-ing the entity ranking protocol.  

## Results
The choice of loss function has by far the highest impact on the performance, followed by the training strategy.  With some exceptions, cross entropy loss performed best across the board.  Although DistMult  outperformed  the  other  models  in  our  study,  we  observed  that,  when  trained consistently,  the  relative  performance  gaps  between  models  are  small. 

 By comparison with the results obtained by the original  [ICLR 20 experiment](https://github.com/uma-pi1/kge-iclr20) using LibKGE on FB15K-237and WNRR, the models performed notably better in my experiment, which can be explained by the domain specific biases in the datasets  used in this experiment.

Below there are the 

#### AIFB

|                                                                                                       |   MRR | Hits@1 | Hits@3 | Hits@10 |                                                                                      Config file |                                                                              Pretrained model |
|-------------------------------------------------------------------------------------------------------|------:|-------:|-------:|--------:|-------------------------------------------------------------------------------------------------:|----------------------------------------------------------------------------------------------:|
| [RESCAL](http://www.icml-2011.org/papers/438_icmlpaper.pdf)                                           | 0.349 |  0.267 |  0.392 |   0.507 |   [config file](https://github.com/Vixci/bachelor/blob/master/best_models/aifb/aifb_aifb-rescal-config-checkpoint_best.yaml) |    1vsAll-kl |
| [TransE](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data) | 0.377 |  0.295 |  0.422 |   0.529 |   [config file](https://github.com/Vixci/bachelor/blob/master/best_models/aifb/aifb_aifb-transe-config-checkpoint_best.yaml) |   NegSamp-kl |
[DistMult](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICLR2015_updated.pdf)  | 0.372 |  0.294 |  0.420 |   0.532 | [config file](https://github.com/Vixci/bachelor/blob/master/best_models/aifb/aifb_aifb-distmult-config-checkpoint_best.yaml) | 1VsAll-kl] |
| [ComplEx](http://proceedings.mlr.press/v48/trouillon16.pdf)                                           | 0.379 |  0.299 |  0.421 |   0.528 |  [config file](https://github.com/Vixci/bachelor/blob/master/best_models/aifb/aifb_aifb-complex-config-checkpoint_best.yaml) |  1VsAll-kl |
| [ConvE](https://arxiv.org/abs/1707.01476)                                                             | 0.373 |  0.294 |  0.414 |   0.522 |    [config file](https://github.com/Vixci/bachelor/blob/master/best_models/aifb/aifb_aifb-conve-config-checkpoint_best.yaml) |     1vsAll-kl |

### MUTAG

|                                                                                                       |   MRR | Hits@1 | Hits@3 | Hits@10 |                                                                                      Config file |                                                                              Pretrained model |
|-------------------------------------------------------------------------------------------------------|------:|-------:|-------:|--------:|-------------------------------------------------------------------------------------------------:|----------------------------------------------------------------------------------------------:|
| [RESCAL](http://www.icml-2011.org/papers/438_icmlpaper.pdf)                                           | 0.321 |  0.259 |  0.349 |   0.445 |   [config file](https://github.com/Vixci/bachelor/blob/master/best_models/aifb/aifb_aifb-rescal-config-checkpoint_best.yaml) |    1vsAll-kl |
| [TransE](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data) | 0.331 |  0.258 |  0.368 |   0.469 |   [config file](https://github.com/Vixci/bachelor/blob/master/best_models/aifb/aifb_aifb-transe-config-checkpoint_best.yaml) |   NegSamp-kl |
[DistMult](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICLR2015_updated.pdf)  | 0.341 |  0.271 |  0.369 |   0.480 | [config file](https://github.com/Vixci/bachelor/blob/master/best_models/aifb/aifb_aifb-distmult-config-checkpoint_best.yaml) | 1VsAll-kl] |
| [ComplEx](http://proceedings.mlr.press/v48/trouillon16.pdf)                                           | 0.330 |  0.263 |  0.361 |   0.469 |  [config file](https://github.com/Vixci/bachelor/blob/master/best_models/aifb/aifb_aifb-complex-config-checkpoint_best.yaml) |  1VsAll-kl |
| [ConvE](https://arxiv.org/abs/1707.01476)                                                             | 0.290 |  0.233 |  0.317 |   0.403 |    [config file](https://github.com/Vixci/bachelor/blob/master/best_models/aifb/aifb_aifb-conve-config-checkpoint_best.yaml) |     1vsAll-kl |

## Reproducing our experiment
Follow the instructions at [LibKGE](https://github.com/uma-pi1/kge) to install it.

Copy the AIFB and MUTAG training/test/valid files in the data folder of kge.
