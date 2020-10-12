#include <iostream>
using namespace std;
const int max_arr = 16;
int search_num = 421;

int recursion_binary_search(int * p, int left_n, int right_n, int num);

int main()
{
	int arr[max_arr] = {1,31,61,91,121,151,181,211,241,271,301,331,361,391,421,999};
	int num = recursion_binary_search(arr, 0 , max_arr,search_num);
	cout << search_num <<"位置为：" << num << endl;
	for (int i = 0; i < max_arr; ++i)
	{
		cout << arr[i] <<"位置为：" << recursion_binary_search(arr,0, max_arr,arr[i]) << endl;
	}
	return 0;
}


int recursion_binary_search(int * p, int left_n, int right_n, int num)
{	
	int min = left_n;
	int max = right_n;
	int mid = (max + min)/2;
	if (p[mid] == num)
		return mid;
	else if (p[mid] > num)
		recursion_binary_search(p, min, mid-1, num);
	else
		recursion_binary_search(p, mid+1, max, num);
}
