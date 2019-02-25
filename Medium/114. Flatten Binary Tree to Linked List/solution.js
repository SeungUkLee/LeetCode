/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    let pre_value = root
    for (const value of preorder(root)) {
        if (value === pre_value)
            continue
        pre_value.left = null
        pre_value.right = value
        pre_value = value
    }
};

function *preorder(root) {
    if (!root)
        return
    const {left, right} = root
    yield root
    yield* preorder(left)
    yield* preorder(right)
}