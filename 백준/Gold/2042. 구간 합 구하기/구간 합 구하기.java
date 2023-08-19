import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeSet;

class Changed implements Comparable<Changed>{
	int no =0;
	long changedNo=0;
	
	public Changed() {

	}
	public Changed(int no) {
		this.no = no;
	}
	
	@Override
	public int compareTo(Changed o) {
	
		return this.no-o.no;
	}
	
}

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] inputNo =str.trim().split(" ");
		int N = Integer.parseInt(inputNo[0]);
		int M = Integer.parseInt(inputNo[1]);
		int K = Integer.parseInt(inputNo[2]);
		long[] arr = new long[N];
		long[] arrSum= new long[N];
		long[] changedArr = new long[N];
		for(int i=0; i<N; i++) {
			arr[i]=Long.parseLong(br.readLine());
			if(i==0) {
			arrSum[i]=arr[i];
			}else {
				arrSum[i]=arrSum[i-1]+arr[i];
				//System.out.println(arrSum[i]);
			}
		}
		TreeSet<Changed> ts= new TreeSet<Changed>();
		Changed[] cArr = new Changed[N];
		for(int i=0; i<N; i++) {
			cArr[i]=new Changed(i);
		}
		for(int i=0; i<M+K; i++) {
			str=br.readLine();
			inputNo=str.trim().split(" ");
			int x = Integer.parseInt(inputNo[0]);
			if(x==1) {
				int y = Integer.parseInt(inputNo[1]);
				long z = Long.parseLong(inputNo[2]);
				cArr[y-1].changedNo=z-arr[y-1];
				ts.add(cArr[y-1]);
			}
			if(x==2) {
				
				int y = Integer.parseInt(inputNo[1]);
				int z = Integer.parseInt(inputNo[2]);
				long sum=0;
				for(Changed c : ts) {
					if(c.no>=y-1&&c.no<z) {
					sum=(long) sum+c.changedNo;}
					else if(c.no>=z) {
						break;
					}
					//System.out.println(sum);
				}
				if(y>1)
				{System.out.println((long)sum+arrSum[z-1]-arrSum[y-2]);}
				else {
				System.out.println((long)sum+arrSum[z-1]);}
			}
		}

	}

}