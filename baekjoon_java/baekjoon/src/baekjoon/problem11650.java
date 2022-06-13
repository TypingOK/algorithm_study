package baekjoon;

import java.io.*;
import java.util.*;

public class problem11650 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[][] a = new int[n][2];
		for(int i =0; i<n; i++) {
			String[] str = br.readLine().split(" ");
			a[i][0]=Integer.parseInt(str[0]);
			a[i][1] = Integer.parseInt(str[1]);
		}
		Arrays.sort(a,new Comparator<int[]>(){
			public int compare(int[] o1, int[] o2) {
				if(o1[0]==o2[0]) {
					return o1[1]-o2[1];
				}
				else {
					return o1[0]-o2[0];
				}
			}
		});
		for(int i=0; i<n; i++) {
			System.out.print(a[i][0]+" "+a[i][1]);
			System.out.println();
		}
	}
	
}
