package baekjoon;

import java.io.BufferedReader;
import java.io.*;
import java.util.*;

public class problem1302 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc = Integer.parseInt(br.readLine());
		Map<String,Integer> book = new HashMap<String,Integer>(); 
		
		for(int i=0; i<tc; i++) {
			String str = br.readLine();
			if(!book.containsKey(str)) {
				book.put(str,1);
			}else {
				int value=book.get(str);
				book.replace(str,value+1);
			}
		}
		int max=0;
		String str = "";
		for (String key: book.keySet()) {
			if(max<book.get(key)) {
				max=book.get(key);
				str = key;
			}else if(max==book.get(key)) {
				if(str.compareTo(key)>0) {
					str=key;
				}
			}
		}
		System.out.println(str);
	}
}
