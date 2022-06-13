package baekjoon;


import java.util.*;
import java.io.*;

public class problem16198 {
	static int N;
	static int max;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		ArrayList<Integer> a = new ArrayList<>();
		String [] str = br.readLine().split(" ");
		for(int i=0; i<N; i++) {
			a.add(Integer.parseInt(str[i]));
		}
		DFS(a,0);
		System.out.println(max);
	}
	
	
	
	static void DFS(ArrayList<Integer> list, int sum) {
		if(list.size()<=2) {
			max = Math.max(sum, max);
			return;
		}
		
		for(int i=1; i<list.size()-1; i++) {
			int temp = list.get(i);
			int num = list.get(i-1) * list.get(i+1);
			list.remove(i);
			DFS(list, sum+num);
			list.add(i,temp);
		}
	}

}
