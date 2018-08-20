class Solution{
    int stringSimilarity(String s) {
        int counter = 0,sLength=s.length();
        for (int i = 1;i < sLength; i++){
            for(int j = 0; j<sLength-i; j++){
                if(s.charAt(j)!=s.charAt(j+i)){
                    break;
                }
                counter+=1;
            }
        }
        return counter+s.length();
    }
}