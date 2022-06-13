package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem5639 {
	static int a[] = new int[10001];
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int index=0;
		String str = br.readLine();
		while(true) {
			a[index++]=Integer.parseInt(str);
			str= br.readLine();
			if(str==null || str.length()==0) {
				break;
			}
		}
		
		postOrder(0,index-1);
	}
	
	static void postOrder(int n,int end) {
		if(n>end) {
			return;
		}else {
			int mid = n+1;
			while(mid<=end && a[mid]<a[n]) {
				mid++;
			}
			postOrder(n+1,mid-1);
			postOrder(mid,end);
			System.out.println(a[n]);
		}
	}

}
