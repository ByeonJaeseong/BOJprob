import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.TreeSet;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] inputNo = str.trim().split(" ");
		int N = Integer.parseInt(inputNo[0]);
		int M = Integer.parseInt(inputNo[1]);
		List<Integer> list = new ArrayList<>(); 
		for(int i=0; i<N; i++) {
			list.add(Integer.parseInt(br.readLine()));
			//집을 번호로 받음
		}
		list.sort(null);//오름차순 정리
		int start = 1;
		int end = list.get(N-1)-list.get(0)+1;
		while(start<end) {
			int midPoint = (start+end)/2;
			int a=list.get(0);
			int num=1;
			for(int i=1; i<N; i++) {
				if((list.get(i)-a)<midPoint) {
					continue;
				}else {
					a=list.get(i);
					num++;
				}
			}
			//System.out.println((midPoint)+" "+(num));
			if(num>=M) {
				start=midPoint+1;
			}else {
				end=midPoint;
			}
		}
		System.out.println(start-1);
	}

}
