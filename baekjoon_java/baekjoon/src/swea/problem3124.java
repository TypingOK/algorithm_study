package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;

public class problem3124 {
	public static class Node implements Comparable<Node>{
		int from;
		int to;
		int weight;
		@Override
		public int compareTo(Node o) {
			
			return this.weight - o.weight;
		}
		public Node() {
		}
		public Node(int from, int to,int weight) {
			this.from=from;
			this.to=to;
			this.weight = weight;
		}
	}
	
	static int N;
	static int[] parents;
	static Node[] edgeList;
	
	public static void makeSet() {
		parents = new int[N];
		
		for(int i=0; i<N; i++) {
			parents[i] = i;
		}
	}
	
	public static int findSet(int a) {
		if(a==parents[a]) return a;
		return parents[a] = findSet(parents[a]);
	}
	
	public static boolean union(int a,int b) {
		int aRoot = findSet(a);
		int bRoot = findSet(b);
		if(aRoot == bRoot) return false;
		parents[bRoot] = aRoot;
		return true;
	}
	
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC =Integer.parseInt(br.readLine());
		for(int tc=1; tc<=TC; tc++) {
			String[] str = br.readLine().split(" ");
			
			N = Integer.parseInt(str[0]);
			int E = Integer.parseInt(str[1]);
			edgeList = new Node[E];
			
			for(int i=0; i<E; i++) {
				str= br.readLine().split(" ");
				int from = Integer.parseInt(str[0])-1;
				int to = Integer.parseInt(str[1])-1;
				int weight = Integer.parseInt(str[2]);
				
				edgeList[i] = new Node(from,to,weight);
			}
			Arrays.sort(edgeList);
			
			makeSet();
			long result=0;
			int cnt=0;
			
			for(Node node : edgeList) {
				if(union(node.from,node.to)) {
					result+=node.weight;
					if(++cnt==N-1) break;
				}
			}
			System.out.println("#"+tc+" "+result);
		}
	}
}
//



//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.Arrays;
//import java.util.LinkedList;
//
//public class problem3124 {
//	public static class Node implements Comparable<Node>{
//		int from;
//		int to;
//		int weight;
//		@Override
//		public int compareTo(Node o) {
//			
//			return this.weight - o.weight;
//		}
//		public Node() {
//		}
//		public Node(int from, int to,int weight) {
//			this.from=from;
//			this.to=to;
//			this.weight = weight;
//		}
//	}
//	
//	static int N;
//	static int[] parents;
//	static Node[] edgeList;
//	
//	public static void makeSet() {
//		parents = new int[N];
//		
//		for(int i=0; i<N; i++) {
//			parents[i] = i;
//		}
//	}
//	
//	public static int findSet(int a) {
//		if(a==parents[a]) return a;
//		return parents[a] = findSet(parents[a]);
//	}
//	
//	public static boolean union(int a,int b) {
//		int aRoot = findSet(a);
//		int bRoot = findSet(b);
//		if(aRoot == bRoot) return false;
//		parents[bRoot] = aRoot;
//		return true;
//	}
//	
//	
//	public static void main(String[] args) throws IOException{
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		int TC =Integer.parseInt(br.readLine());
//		for(int tc=1; tc<=TC; tc++) {
//			String[] str = br.readLine().split(" ");
//			
//			N = Integer.parseInt(str[0]);
//			int E = Integer.parseInt(str[1]);
//			edgeList = new Node[E];
//			
//			for(int i=0; i<E; i++) {
//				str= br.readLine().split(" ");
//				int from = Integer.parseInt(str[0])-1;
//				int to = Integer.parseInt(str[1])-1;
//				int weight = Integer.parseInt(str[2]);
//				
//				edgeList[i] = new Node(from,to,weight);
//			}
//			Arrays.sort(edgeList);
//			
//			makeSet();
//			long result=0;
//			int cnt=0;
//			
//			for(Node node : edgeList) {
//				if(union(node.from,node.to)) {
//					result+=node.weight;
//					if(++cnt==N-1) break;
//				}
//			}
//			System.out.println("#"+tc+" "+result);
//		}
//	}
//}
