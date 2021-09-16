var search = function(arr, target) {
    let low = 0;
    let high = arr.length-1;
    let mid = 0;
    while(low<=high){
        mid = low + Math.floor((high - low)/2);
        if(target==arr[mid]){
            return mid;
        }
        if(target<arr[mid]){
            high = mid-1;
        }
        else if(target > arr[mid]){
            low = mid+1
        }
    }
    return -1;
};