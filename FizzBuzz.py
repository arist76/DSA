class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        count = 1
        
        if type(n) == str:
            print('this is an invalid error')
            return
        
        while count <= int(n):
            if count%3==0 and count%5==0:
                answer.append('FizzBuzz')
                
            elif count%3==0:
                answer.append('Fizz')
                
            elif count%5==0:
                answer.append('Buzz')
                
            else:
                answer.append(str(count))
                
            count += 1
                
                
        return answer
            
            