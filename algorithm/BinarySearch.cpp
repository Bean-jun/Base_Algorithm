#include <iostream>
using namespace std;
const int max_arr = 16;
int search_num = 421;

int binary_search(int * p, int n, int num);

int main()
{
	int arr[max_arr] = {1,31,61,91,121,151,181,211,241,271,301,331,361,391,421,999};
	int num = binary_search(arr,max_arr,search_num);
	cout << search_num <<"位置为：" << num << endl;
	for (int i = 0; i < max_arr; ++i)
	{
		cout << arr[i] <<"位置为：" << binary_search(arr,max_arr,arr[i]) << endl;
	}
	return 0;
}


int binary_search(int *p, int n, int num)
{	
	int min = 0;
	int max = n;
	int mid;
	while (min <= max)
		{	
			mid = (max + min)/2;
			if (p[mid] == num)
				return mid;
			else if (p[mid] > num)
				max = mid-1;
			else
				min = mid+1;
		} 
	return -1;
}
