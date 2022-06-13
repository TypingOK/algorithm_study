package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem2822 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] a = new int[8];
		int max = 0;
		int index=-1;
		int[] arr = new int[8];
		for(int i=0; i<8; i++) {
			a[i]=Integer.parseInt(br.readLine());
		}
		int sum=0;
		for(int i=0; i<5; i++) {
			for(int j=0; j<8; j++) {
				if(a[j]>max) {
					max=a[j];
					index=j;
				}
			}
			sum+=max;
			arr[index]++;
			a[index]=0;
			index=-1;
			max=0;
		}
		System.out.println(sum);
		for(int i=0; i<8; i++) {
			if(arr[i]==1) {
				
				System.out.print((i+1)+" ");
			}
		}
	}

}
