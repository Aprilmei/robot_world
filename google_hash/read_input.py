
def read_google(filename):
    
    data = dict()

    with open(filename, "r") as fin:
        #read one line 
        system_desc = next(fin)
        number_of_videos, number_of_endpoints, number_of_requests, number_of_caches, cache_size= system_desc.split(" ")
        number_of_videos = int(number_of_videos)
        number_of_endpoints = int(number_of_endpoints)
        number_of_requests = int(number_of_requests)
        number_of_caches = int(number_of_caches)
        cache_size = int(cache_size)
        
        
        video_size_desc = next(fin).strip().split(" ")
        for i in range(len(video_size_desc)):
            video_size_desc[i] = int(video_size_desc[i])
            
        video_ed_request = dict()
        ed_cache_list = []

        ### CACHE SECTION
        ep_to_cache_latency = [] 

        ep_to_dc_latency = [] 
        for i in range(number_of_endpoints):

            ep_to_dc_latency.append([])
            ep_to_cache_latency.append([])

            dc_latency, number_of_cache_i = next(fin).strip().split(" ")
            dc_latency = int(dc_latency)
            number_of_cache_i = int(number_of_cache_i)

            ep_to_dc_latency[i] = dc_latency

            for j in range(number_of_caches):
                ep_to_cache_latency[i].append(ep_to_dc_latency[i]+1)

            cache_list = []
            for j in range(number_of_cache_i):
                cache_id, latency = next(fin).strip().split(" ")
                cache_id = int(cache_id)
                cache_list.append(cache_id)
                latency = int(latency)
                ep_to_cache_latency[i][cache_id] = latency

            ed_cache_list.append(cache_list)

        ### REQUEST SECTION
        for i in range(number_of_requests):
            video_id, ed_id, requests = next(fin).strip().split(" ")
            video_ed_request[(video_id,ed_id)] = requests

    
    data["number_of_videos"] = number_of_videos
    data["number_of_endpoints"] = number_of_endpoints
    #the number of the requests from endpoint to videos 
    data["number_of_requests"] = number_of_requests
    data["number_of_caches"] = number_of_caches
    data["cache_size"] = cache_size
    #The size of every video 
    data["video_size_desc"] = video_size_desc
    #The end point to DC latency 
    data["ep_to_dc_latency"] = ep_to_dc_latency
    #the end point to cache server latency 
    data["ep_to_cache_latency"] = ep_to_cache_latency
    #The end point connection to cache server 
    data["ed_cache_list"] = ed_cache_list
    
    # the request number of the requests from end point to videos
    data["video_ed_request"] = video_ed_request

    return data

def print_result(file):
    
    data = read_google(file)
    
    n=0
    for key in data["video_ed_request"]:
        print(key[0],key[1],data["video_ed_request"][key])
        
    print("number of  requests ",data["number_of_requests"])
    sum_number = 0
    

    
    for i in data["video_ed_request"]:
       
        sum_number += int(data["video_ed_request"][i])
        n+=1
    #print(" ep_to_dc_latency",data["ep_to_dc_latency"])
    #print(" ep_to_cache_latency",data["ep_to_cache_latency"])
    #print(" The end point connection to cache server ", data["ed_cache_list"])
    print("the number of requests",n)
    print("number of individual requests=", sum_number, " which is different from the number of request descriptions ", data["number_of_requests"])


 

if __name__ == "__main__":
    print_result("input/me_at_the_zoo.in")
    #print_result("input/trending_today.in")
    #print_result("input/google_example.in")
    
else:
    pass

'''
print("Number of vides", data["number_of_videos"])
print("Number of end points",data["number_of_endpoints"])
print(" number_of_requests",data["number_of_requests"])
print("number_of_caches ", data["number_of_caches"])
print(" cache_size",data["cache_size"])

print(" video_size_desc", data["video_size_desc"])

print(" ep_to_dc_latency",data["ep_to_dc_latency"])
print(" ep_to_cache_latency",data["ep_to_cache_latency"])

print("The end point connection to cache server ",data["ed_cache_list"])


for key in data["video_ed_request"]:
    print(key,data["video_ed_request"][key])
'''
    
