package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class problem1764 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int n=Integer.parseInt(str[0]);
		int m=Integer.parseInt(str[1]);
		Map<String,Integer> m1 = new HashMap<String,Integer>();
		
		for(int i=0; i<n; i++) {
			m1.put(br.readLine(),1);
		}
		for(int i=0; i<m; i++) {
			String s = br.readLine();
			if(m1.get(s)!=null) {
				m1.replace(s,2);
			}
		}
		List<String> list = new ArrayList<String>();
		Set<String> keySet = new HashSet<String>(m1.keySet());
		
		for(String key : keySet) {
			if(m1.get(key)==2) {
				list.add(key);
			}
		}
		Collections.sort(list);
		System.out.println(list.size());
		for(int i=0; i<list.size(); i++) {
			System.out.println(list.get(i));
		}
	}

}
