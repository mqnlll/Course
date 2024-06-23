#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

long long int cnt = 0;
void merge_sort(int arr[], int temp[], int l, int r) {
	if ((r - l) == 0 || (r - l) == 1) {
		return;
	}
	int r1= ((r - l) >> 1 )+ l;
	int l2 = r1;
	merge_sort(arr, temp, l, r1);
	merge_sort(arr, temp, l2, r);
	int i = l, j = l2,k=l;
	while (i != r1 && j!=r) {
		if (arr[i] < arr[j]) {
			temp[k] = arr[j];
			cnt += j - k;
			j += 1;
		}
		else {
			temp[k] = arr[i];
			i += 1;
		}
		k++;
	}
	while (i != r1) {
		temp[k] = arr[i];
		++i; ++k;
	}
	while (j != r) {
		temp[k] = arr[j];
		++j; ++k;
	}
	for (int k = l; k < r; k++) {
		arr[k] = temp[k];
	}
}

int main()
{
	int n;
	int arr[100001];
	int temp[100001];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	merge_sort(arr, temp, 0, n);
	printf("%lld", cnt);
}