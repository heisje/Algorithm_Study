#include <iostream>
#include <vector>
using namespace std;


struct TreeNode {
	int key;
	TreeNode* left;
	TreeNode* right;
};
TreeNode* new_node(int key) {
	TreeNode* temp = new TreeNode;
	temp->key = key;
	temp->left = temp->right = NULL;
	return temp;

}
TreeNode* insert_node(TreeNode* node, int key) {
	if (node == NULL) return new_node(key);
	if (key < node->key) node->left = insert_node(node->left, key);
	else if (key > node->key) node->right = insert_node(node->right, key);

	return node;
}
TreeNode* search_node(TreeNode* node, int key) {
	if (node == NULL)return node;
	if (key < node->key) node = search_node(node->left, key);
	else if (key > node->key)node = search_node(node->right, key);

	return node;
}

TreeNode* min_value_node(TreeNode* node)
{
	TreeNode* current = node;
	while (current->left != NULL) {
		current = current->left;
	}
	return current;

}

TreeNode* delete_node(TreeNode* node, int key)
{
	if (node == NULL)return node;
	if (key < node->key)node->left = delete_node(node->left, key);
	else if (key > node->key)node->right = delete_node(node->right, key);
	else {
		if (node->left == NULL)
		{
			TreeNode* temp = node->right;
			delete node;
			return temp;

		}
		else if (node->right == NULL)
		{
			TreeNode* temp = node->left;
			delete node;
			return temp;

		}
		else {
			TreeNode* temp = min_value_node(node->right);
			node->key = temp->key;
			node->right = delete_node(node->right, temp->key);
		}
	}

	return node;
}


void inorder(TreeNode* node)
{
	cout << "test";
	if (node) {
		inorder(node->left);
		cout << node->key << " ";
		inorder(node->right);
	}
}
int main() {
	TreeNode* node = NULL;
	int N;
	cin >> N;
	int* arr = new int[N];		// 동적할당

	int minus_idx;
	
	cout << N << endl;

	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		arr[i] = tmp;
		if (tmp == -1) {
			minus_idx = i;
		}
	}
	
	int new_num;
	cin >> new_num;

	cout << new_num << endl;
	arr[minus_idx] = new_num;

	for (int i = 0; i < N; i++) {
		cout << arr[i] << endl;
		insert_node(node, arr[i]);
	}

	if (search_node(node, 10 )) cout << "찾는 노드가 있음 " << endl;

	inorder(node);
	delete[] arr;
}