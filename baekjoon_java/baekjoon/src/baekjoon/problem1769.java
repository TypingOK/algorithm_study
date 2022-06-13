package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class problem1769 {

	public static void main(String[] args) throws IOException{
//		Scanner sc= new Scanner(System.in);
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		String str =br.readLine();
		int[] arr=new int[str.length()];
		for(int i=0; i<arr.length; i++) {
			arr[i]=Integer.valueOf(str.charAt(i)-'0');
		}
		Q(0,arr);
	}
	static void Q(int idx,int[] arr) {
		if(arr.length==1) {
			System.out.println(idx);
			if(arr[0]%3==0) {
				System.out.println("YES");
			}
			else {
				System.out.println("NO");
			}
			return;
		}
		long sum=0;
		for(int i=0; i<arr.length; i++) {
			sum+=arr[i];
		}
		int sumLength=(int)(Math.log10(sum)+1);
		int[] temp = new int[sumLength];
		for(int i=0; i<temp.length; i++) {
			temp[i]=(int)(sum%10);
			sum=sum/10;
		}
		Q(idx+1, temp);
		
	}

}
