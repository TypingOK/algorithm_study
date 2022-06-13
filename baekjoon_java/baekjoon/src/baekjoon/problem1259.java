package baekjoon;

import java.io.*;

public class problem1259 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str= "";
		while (true) {
			str=br.readLine();
			if(str.equals("0")) {
				break;
			};
			if(str.length()%2==1) {
				int mid = str.length()/2;
				String subLeft = str.substring(0, mid);
				String subRight = str.substring(mid+1);
				StringBuffer sb = new StringBuffer(subRight);
				subRight=sb.reverse().toString();
				if(subLeft.equals(subRight)) {
					System.out.println("yes");
				}else {
					System.out.println("no");
				}
			}
			else {
				int mid = str.length()/2;
				String subLeft = str.substring(0, mid);
				String subRight = str.substring(mid);
				StringBuffer sb = new StringBuffer(subRight);
				subRight=sb.reverse().toString();
				if(subLeft.equals(subRight)) {
					System.out.println("yes");
				}else {
					System.out.println("no");
				}
			}
		}
	}

}
