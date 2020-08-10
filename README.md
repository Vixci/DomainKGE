# Re-evaluating Knowledge Graph Embedding Models on Domain Specific Datasets:

This experiment aims to answer the question on whether KGE models perform differently on domain specific datasets compared to generic ones like Freebase and Wordnet, which are commonly used in ML benchmarks.

I conducted the experiment using the [LibKGE](https://github.com/uma-pi1/kge) framework. This project includes the data dumps used for AIFB and MUTAG, the CSV files with all trials as well as the the best model configurations yaml files.

I used  two  domain  specific  datasets  (AIFB and  MUTAG),  both  bound  by  strong  ontological  information.   The experiment aims to  explain how hyperparameters affect KGE model performance on domain specific datasets by searching across a large hyperparameter space and then evaluating performance us-ing the entity ranking protocol.  

## Results
The choice of loss function has by far the highest impact on the performance, followed by the training strategy.  With some exceptions, cross entropy loss performed best across the board.  Although DistMult  outperformed  the  other  models  in  our  study,  we  observed  that,  when  trained consistently,  the  relative  performance  gaps  between  models  are  small.   Our  results are further compared with the ones obtained by  the original  [ICLR 20 experiment] (https://github.com/uma-pi1/kge-iclr20) on FB15K-237and WNRR. Both experiments use their Pytorch-based libkge framework allowing for  equivalent  methodologies  in  both  studies  and  thus  commensurate  results  across the range of configurations.  The models performed notably better in my experiment,which can be explained by the domain specific biases in the datasets  used in this experiment.

