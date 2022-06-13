package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class problem1647 {
	static class Node implements Comparable<Node>{
		int from,to,weight;
		Node(int from, int to,int weight){
			this.from = from;
			this.to=to;
			this.weight=weight;
		}
		@Override
		public int compareTo(Node o) {
			return this.weight-o.weight;
		}
	}
	
	static void makeSet() {
		parents = new int[N+1];
		for(int i=1; i<N+1; i++) {
			parents[i]=i;
		}
	}
	static int findSet(int a) {
		if(a==parents[a]) return a;
		
		return parents[a]=findSet(parents[a]);
	}
	static boolean unionSet(int a, int b) {
		int aRoot = findSet(a);
		int bRoot = findSet(b);
		
		if(aRoot==bRoot) {
			return false;
		}
		parents[bRoot] = aRoot;
		return true;
	}
	static int N;
	static int M;
	static int[] parents;
	static Node[] node;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" " );
		N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		node = new Node[M];
		for(int i=0; i<M; i++) {
			str = br.readLine().split(" ");
			int a = Integer.parseInt(str[0]);
			int b = Integer.parseInt(str[1]);
			int c = Integer.parseInt(str[2]);
			node[i]=new Node(a,b,c);
		}
		Arrays.sort(node);
		makeSet();
		int result=0;
		int bigCost=0;
		for(int i=0; i<M; i++) {
			if(unionSet(node[i].from, node[i].to)) {
				result+=node[i].weight;
				bigCost = node[i].weight;
			}
		}
		System.out.println(result-bigCost);
	}

}
