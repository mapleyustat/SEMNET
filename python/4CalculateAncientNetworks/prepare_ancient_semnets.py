import numpy as np

def remove_blacklist_words(network_T,nn,all_KW):
    # TODO: remove words that have degree>max_degree, for instance degree>100.000
    return network_T,nn,all_KW


def create_ancient_networks(network_T,nn,all_KW,y_start,y_end):
    network_T,nn,all_KW=remove_blacklist_words(network_T,nn,all_KW)
    
    ancient_nns=[]
    ancient_nums=[]
    
    # probably quite inefficient method
    for year in range(y_start,y_end):
        curr_nn=np.zeros(network_T.shape)
        for ccx in range(len(network_T)):
            all_ids=[]
            for ccy in range(len(network_T)):
                curr_entry=network_T[ccx,ccy]
                count=0
                for ccn in range(len(curr_entry)):
                    # curr_entry[ccn] is a number in the form: YYYY.paper_id, see create_network()
                    if curr_entry[ccn]<year+1: 
                        count+=1
                    all_ids.append(curr_entry[ccn])
                curr_nn[ccx,ccy]=count
        ancient_nns.append(curr_nn)
        
        ancient_nums=len(set(all_ids))
        print('create_ancient_networks: Finished year ', year)
        
    return(all_KW,ancient_nns,ancient_nums)
        
    
                