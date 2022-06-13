package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem1235 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String[] str =new String[n];
		for(int i = 0; i<n; i++) {
			str[i]=br.readLine();
		}
		int flag=0;
		int cnt=0;
		for(int k=str[0].length()-1; k>=0; k--) {
			if(flag==1) {
				break;
			}
			flag=0;
				for(int i=0; i<n; i++) {
					if(flag==1) {
						break;
					}
					else if(flag==-1) {
						break;
					}
					for(int j=i+1; j<n; j++) {
//						System.out.print(str[i].substring(k,strlength)+" "+str[j].substring(k,strlength)+" "+str[i].substring(k,strlength).equals(str[j].substring(k,strlength)));
						if(str[i].substring(k).equals(str[j].substring(k))) {
							flag=-1;
							break;
						}else {
							flag=1;
						}
					}
					System.out.println();
				}
			cnt++;
		}
		System.out.println(cnt);
	}

}
