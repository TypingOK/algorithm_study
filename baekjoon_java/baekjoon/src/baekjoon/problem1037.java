package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class problem1037 {
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int[] a = new int [num];
		for(int i=0; i<num;i++) {
			a[i]=Integer.parseInt(st.nextToken());
		}
		
		int iMax=0;
		int iMin=9999999;
		for(int i: a) {
			iMax=Math.max(iMax, i);
		}
		for(int i:a) {
			iMin=Math.min(iMin, i);
		}
		System.out.println(iMax*iMin);
	}

}
