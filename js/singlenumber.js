/**
 *
 * Created by Zhenyu on 5/25/15.
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var r = 0;
    for (var i = 0; i < nums.length; i ++){
        console.log(i);
        r = r ^ nums[i];
    }
    return r;

};

a = [1,1,2];
console.log(singleNumber(a));
