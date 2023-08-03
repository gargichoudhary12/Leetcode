/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
   bool hasPathSum(TreeNode* root, int targetSum, int curr=0) {
        if(!root)   return 0;
        if(!root->left && !root->right) return curr+root->val == targetSum;
        return hasPathSum(root->left, targetSum, curr+root->val) || hasPathSum(root->right, targetSum, curr+root->val);
    }
};