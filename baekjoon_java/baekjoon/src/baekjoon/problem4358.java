package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class problem4358 {
	
	public static class Tree implements Comparable<Tree>{
		String name;
		double num;
		public Tree(String key, double integer) {
			this.name=key;
			this.num=integer;
		}
		@Override
		public int compareTo(Tree o) {
			return this.name.compareTo(o.name);
		}
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		HashMap<String, Integer> map = new HashMap<>();
		ArrayList<Tree> list = new ArrayList<>();
		
		int count = 0;
		String tree = br.readLine();
		while(true) {
			if(map.containsKey(tree)) {
				map.replace(tree, map.get(tree)+1);
			}else {
				map.put(tree, 1);
			}
			count+=1;
			
			tree = br.readLine();
			if(tree==null||tree.length()==0) {
				break;
			}
		}
		for(String key : map.keySet()) {
			list.add(new Tree(key,map.get(key)));
		}
		
		Collections.sort(list);
		
		int size = list.size();
		
		for(int i=0; i<size; i++) {
			System.out.print(list.get(i).name+" ");
			System.out.printf("%.4f",list.get(i).num*100/count);
			System.out.println();
		}
		
	}

}
