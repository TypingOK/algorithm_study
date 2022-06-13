package baekjoon;

import java.io.BufferedReader;
import java.io.*;

public class problem9655 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n =Integer.parseInt(br.readLine());
		boolean turn=false;
		while(n>0) {
			if(n>=3) {
				n-=3;
				turn= !(turn);
			}
			else {
				n-=1;
				turn= !(turn);
			}
		}
		if(turn) {
			System.out.println("SK");
		}
		else {
			System.out.println("CY");
		}
	}

}
