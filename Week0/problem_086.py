#PROBLEM 86 - CLUSTERING PATTERN ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = clustering_engine("kmeans", "group123●cluster456○center◐analysis", 2, 3, 1)
    result2 = clustering_engine("hierarchical", "tree248●node567○branch", 1, 2, 2)
    result3 = clustering_engine("density", "region135○dense◐sparse", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def clustering_engine(clustering_method, cluster_data, similarity_threshold, cluster_iterations, precision_level):
    #Step 1: Count Clustering Elements

    #dataset_size: Count total characters in cluster_data
    dataset_size = len(cluster_data)
    #data_points: Count digit characters (0-9) in cluster_data
    data_points = cluster_data.count("0")+ cluster_data.count("1")+ cluster_data.count("2")+cluster_data.count("3")+ cluster_data.count("4")+ cluster_data.count("5")+ cluster_data.count("6")+ cluster_data.count("7")+cluster_data.count("8")+ cluster_data.count("9")
    #cluster_markers: Count cluster indicator characters ("●", "○", "◐") in cluster_data
    cluster_markers = cluster_data.count("●")+ cluster_data.count("○")+ cluster_data.count("◐") 

    Clustering_Complexity_Score = (dataset_size * 19) + (data_points * 38) + (cluster_markers * 80)
    Clustering_Multiplier = 6.6*(clustering_method=="kmeans") + 6.1*(clustering_method=="hierarchical") + 5.7*(clustering_method=="density")
    Cluster_Formation_Projection =  Clustering_Complexity_Score *  Clustering_Multiplier * cluster_iterations
    Raw_Clustering_Quality_Index = Cluster_Formation_Projection  - (similarity_threshold * 210)
    Clustering_Quality_Index = Raw_Clustering_Quality_Index *(Raw_Clustering_Quality_Index >=420) + 420*(Raw_Clustering_Quality_Index <420)
    Data_Point_Distribution_Ratio = data_points / (dataset_size + (dataset_size==0)) *(dataset_size!=0) + 2*(dataset_size==0)
    Clustering_Precision = (Data_Point_Distribution_Ratio  * 100) + (cluster_iterations * 105)
    Clustering_Method_Complexity = 9*(clustering_method=="kmeans") + 11*(clustering_method=="hierarchical") + 13*(clustering_method=="density")
    Quality_Categories = "Tight_Clustering"*(Clustering_Quality_Index>=1050) + " Moderate_Clustering"*(780<=Clustering_Quality_Index<1050) + "Loose_Clustering"*(Clustering_Quality_Index<780)
    Iteration_Categories = "Iterative_Clustering"*( cluster_iterations == 3) + "Standard_Clustering"*( cluster_iterations == 2) + "Quick_Clustering"*( cluster_iterations == 1) 
    Cluster_Cohesion = (cluster_markers * 200) / (data_points+(data_points==0)) * (data_points!=0) + 220*(data_points==0)
    Clustering_Signature = clustering_method + str(cluster_iterations) + str(similarity_threshold) + Quality_Categories 

    return f"CLUSTERED: {Iteration_Categories} | METHOD: {clustering_method} | SIZE: {dataset_size} | POINTS: {data_points} | MARKERS: {cluster_markers} | INDEX: {Clustering_Quality_Index:.1f} | PRECISION: {Clustering_Precision:.1f}% | DISTRIBUTION: {Data_Point_Distribution_Ratio:.3f} | COHESION: {Cluster_Cohesion:.1f}% | CATEGORY: {Quality_Categories} | COMPLEXITY: {Clustering_Method_Complexity} | SIG: {Clustering_Signature}"

main()
