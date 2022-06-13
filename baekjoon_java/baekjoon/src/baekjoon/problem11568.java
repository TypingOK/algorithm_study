package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class problem11568 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		ArrayList<Integer> dp = new ArrayList<Integer>();
		String str[] = br.readLine().split(" ");
		dp.add(Integer.parseInt(str[0]));
		
		for (int i = 1; i < N; i++) {
			int a = Integer.parseInt(str[i]);
			for (int j = 0; j < dp.size(); j++) {

				if (dp.get(j) >= a) {
					dp.remove(j);
					dp.add(j,a);
					
					break;
				}
				
				if(j==dp.size()-1) {
					dp.add(a);
				}
			}
		}
		System.out.println(dp.size());
	}

}
