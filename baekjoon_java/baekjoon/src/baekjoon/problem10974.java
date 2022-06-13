package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem10974 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		boolean[] visited = new boolean[n];
		int[] arr = new int[n];
		int[] output = new int[n];
		for(int i =0; i<n; i++) {
			arr[i]=i+1;
		}
		perm(arr,output,visited,0,n);
	}
	public static void perm(int[] arr, int[] output, boolean[] visited, int depth, int n) {
		if(depth == n) {
			print(output, n);
			return ;
		}
		
		for(int i=0; i<n; i++) {
			if(visited[i] != true) {
				visited[i]=true;
				output[depth]= arr[i];
				perm(arr, output,visited,depth+1, n);
				visited[i]=false;
			}
		}
	}
	public static void print(int[] arr, int n) {
		for(int i=0; i<n; i++) {
			System.out.print(arr[i]+" ");
		}
		System.out.println();
	}
}
