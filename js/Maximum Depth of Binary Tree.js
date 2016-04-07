/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

var maxDepth = function(root) {
    return function(node){
        if (node === null){
            return 0;
        }
        left = find(node.left) + 1;
        right = find(node.right) + 1;
        if (left > right)
            return left;
        else
            return right;
    }(node);


};

console.log("hello");