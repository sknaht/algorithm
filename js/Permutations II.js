/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    var tmp = {};
    for (var i = 0; i < nums.length; i++){
        if (nums[i] in tmp){
            tmp[nums[i]]++;
        }else tmp[nums[i]] = 1;
    }
    console.log(JSON.stringify(tmp));
    var result = [];
    var f = function(result, path, tmp, k){
        if (k === 0){
            result.push([].concat(path));
            return
        }
        for (var key in tmp){
            if (tmp[key] > 0){
                tmp[key]--;
                f(result, path.concat([key]), tmp, k - 1);
                tmp[key]++;
            }
        }
    };

    f(result, [], tmp, nums.length);
    console.log(JSON.stringify(result));
    return result

};

permuteUnique([1,1,2]);