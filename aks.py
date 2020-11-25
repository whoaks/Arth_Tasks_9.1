import pyaudio
import os
import speech_recognition as sr
import pyttsx3 as p 

r=sr.Recognizer()

print('\t\t\t\t\t\t     Automation Configuration    ')
p.speak('Automation Configuration')
print("\t\t\t\t\t\t-------------------------------- ")
print()
print()

while True:
    print("\t\t\t\t\tStart Namenode")
    print("\t\t\t\t\tStart DataNode")
    print('\t\t\t\t\tConfigure webserver')
    print('\t\t\t\t\tCreate virtual group')
    print('\t\t\t\t\tCreate LVM')
    print('\t\t\t\t\tAttach More Harddisks to Virtual Group dynamically')
    print('\t\t\t\t\tIncrease Logical Volume ( Partition ) Size dynamically')
    print("\t\t\t\t\tConfigure AWS Cloud")
    print('\t\t\t\t\tPrediction Automation')
    print('\t\t\t\t\tAutomate Docker Container')
    print()

    with sr.Microphone() as source:
        print('\t\t\t\t\tPlease tell what you want to do :-')
        audio=r.listen(source)

    option=r.recognize_google(audio)
    option=option.lower()
    print(option)
  #  p.speak('Please tell me what you want')
  #  option=input('Enter :-  ')

    if option=='configure aws cloud' or option=='configure a ws cloud' or option=='configure a w s cloud' or option=='configure aw s cloud' or option=='configure cloud' or option=='configure a w s' or option=='1':
        while True:

            p.speak('Configuring AWS cloud')
            
            print('\t\t\t\t\tCreate Key Pair')
            print('\t\t\t\t\tCreate Security Group')
            print('\t\t\t\t\tAdd Ingress Rules to Existing Security Group')
            print('\t\t\t\t\tLaunch Instance on Cloud')
            print('\t\t\t\t\tCreate EBS Volume')
            print('\t\t\t\t\tAttach EBS Volume to EC2 Instance')
            print('\t\t\t\t\tConfigure WebServer')
            print('\t\t\t\t\tCreate Static Partiton and Mount /var/www/html folder on EBS volume')
            print('\t\t\t\t\tCreate S3 Bucket')
            print('\t\t\t\t\tput Object inside S3 bucket and make it public accessible')
            print('\t\t\t\t\tremove specific Object from S3 bucket')
            print('\t\t\t\t\tdelete Specific S3 Bucket')
            print('\t\t\t\t\tcreate Cloudfront distribution providing S3 as Origin')
            print('\t\t\t\t\tdelete Key Pair')
            print('\t\t\t\t\tStop EC2-Instances')
            print('\t\t\t\t\tStart Ec2-Instances')
            print('\t\t\t\t\tterminate Ec2-Instances')
            print('\t\t\t\t\tdelete Security group')

            with sr.Microphone() as source:
                print('What you want to configure on cloud')
                audio=r.listen(source)
            
            ch2=r.recognize_google(audio)
            ch2=ch2.lower()
            print(ch2)
           # p.speak('What you want to configure on cloud')
           # ch2=input('Enter :-  ')
            
            if ch2=='create key pair':
                p.speak('Enter key name to create')
                key_name=input('key name to create :-  ')
                print(key_name)
                os.system('aws ec2 create-key-pair --key-name {}'.format(key_name))
                p.speak('keypair created')
            
            elif ch2=='launch ec2 instance' or ch2=='create instance' or ch2=='launch instance' or ch2=='launch ec2' :
                
                p.speak('Enter Instance type')
                itype=input('Instance type :-   ')
                p.speak('Enter Number of Instace')
                count=input('Number of Instance :-  ')
                p.speak('Enter key name to attach it to Ec2 Instance :-  ')
                key=input('key name to attach it to Ec2 Instance :-  ')
                os.system('aws ec2 run-instances --image-id ami-0a9d27a9f4f5c0efc --instance-type {} --count {} --subnet-id subnet-0892eab4da13f00a5 --security-group-ids sg-0f7296c8f424d39c0 --key-name {}'.format(itype , count , key))
            
            elif ch2=='create ebs volume' or ch2=='create volume' or ch2=='create e bs volume' or ch2=='create ebs  volume' or ch2=='create EPS volume' or ch2=='1':
                p.speak('Creation of EBS Volume')

                p.speak('Please Enter size of EBS Volume')
                ebs_size=input('Enter size of EBS Volume :-   ')                
                os.system('aws ec2 create-volume --availability-zone ap-south-1a --size {}'.format(ebs_size))
            
            #elif cmd2=='2':
            elif ch2=='create security group' or ch2=='create sg':
                p.speak('Enter Security name to create')
                sg_name=input('Security name to create :-  ')
                os.system('aws ec2 create-security-group --group-name {} --description "SG Created" --vpc-id vpc-089aab5d2c0b4f90c'.format(sg_name))
                p.speak('security group created')
            
            #elif cmd2=='3':
            elif ch2=='add ingress rules' or ch2=='add ingres rule' or ch2=='add ingres rules' or ch2=='add Ingress rule' or ch2=='add Ingress rules':
                p.speak('Enter Security Group Id')
                sg_id=input('Security Group Id :-  ')
                p.speak('Enter IP Protocol ( ie. tcp )')
                ip_protocol=input('IP Protocol :-   ')
                p.speak('Enter Port number')
                port_no=input('Port no :-   ')
                p.speak('Enter CidrIp')
                cidr=input('Cidr IP :-   ')
                os.system('aws ec2 authorize-security-group-ingress --group-id {} --ip-permissions IpProtocol={},FromPort={},ToPort={},IpRanges=[{}]'.format(sg_id , ip_protocol , port_no , port_no ,cidr))
            
            
            
            #elif cmd2=='6':
            elif ch2=='attach ebs volume to ec2 instance' or ch2=='attach volume to ec2 instance' or ch2=='attach volume to ec2' or ch2=='attach ebs volume':
                p.speak('Enter EBS Volume ID to Attach to EC2 Instance')
                ebs_vid=input('EBS Volume ID to Attach to EC2 Instance :-  ')
                p.speak('Enter EC2 Instance ID to attach EBS Volume')
                ec2_id=input('EC2 Instance ID to attach EBS Volume :-  ')
                os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(ebs_vid , ec2_id))
            
            #elif cmd2=='8':
            elif ch2=='create partition':
                print('Enter Ip Address to Remote Login :-  ', end='')
                ip=input()
                print('Enter Keyname :-  ', end='')
                key=input()
                os.system('ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/xvdf'.format(ip , key))
                print('Enter Partition Name to format and  Mount /var/www/html folder  :-   ', end='')
                name=input()
                os.system('ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{}'.format(ip , key , name))
                os.system('ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html'.format(ip , key , name))
            
            #elif cmd2=='9':
            elif ch2=='create s3 bucket' or ch2=='create sthree bucket' or ch2=='create s three bucket' or ch2=='create S3 bucket' or ch2=='2':
                p.speak('Creation   of S3    bucket')
                p.speak('Enter S3 bucket name that must be unique')
                s3_name=input('S3 bucket name that must be unique :-  ')
                os.system('aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1'.format(s3_name))
                p.speak('S3 bucket created')
            
            #elif cmd2=='10':
            elif ch2=='upload object in s3 bucket' or ch2=='upload object in bucket' or ch2=='upload object in s three bucket' or ch2=='3':
                p.speak('upload object in s3 bucket')
                p.speak('Enter object name to put inside S3 bucket')
                object_name=input('object name to put inside S3 bucket :-   ')
                p.speak('Enter S3 bucket')
                s3_name=input('S3 bucket :-  ')
                os.system('aws s3 cp {}.jpg s3://{} --acl public-read'.format(object_name , s3_name))
            
            elif ch2=='remove object from S3 bucket' or ch2=='remove object from sthree bucket' or ch2=='remove object from s three bucket' :
                
                with sr.Microphone() as source:
                    print('Enter S3 Bucket name :-  ')
                    audio=r.listen(source)
                
                s3_name=r.recognize_google(audio)
                s3_name=s3_name.lower()
                print(s3_name)

                print('Enter object name :-  ', end='')
                object_name=input()
                
                os.system('aws s3 rm s3://{}/{}'.format(s3_name , object_name))
            
            elif ch2=='delete S3 bucket' or ch2=='delete sthree bucket' or ch2=='delete s three bucket':
                with sr.Microphone() as source:
                    print('Enter S3 Bucket name :-  ')
                    audio=r.listen(source)
                
                s3_name=r.recognize_google(audio)
                s3_name=s3_name.lower()
                print(s3_name)

                os.system('aws s3api delete-bucket --bucket {} --region ap-south-1'.format(s3_name))
            
            #elif cmd2=='13':
            elif ch2=='create cloud front' or ch2=='create cloudfront' or ch2=='create c d n' or ch2=='create cd n' or ch2=='create cdn'or ch2=='create c d n' or ch2=='4':
                p.speak('creation   of   cloud front')
                p.speak('Enter S3 bucket')
                s3_name=input('S3 bucket :-  ')
                
                os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(s3_name))
            
            #elif cmd2=='14': 
            elif ch2=='delete key pair':
                with sr.Microphone() as source:
                    print('Enter key name to delete :-  ')
                    audio=r.listen(source)
                
                key_name=r.recognize_google(audio)
                key_name=key_name.lower()
                print(key_name)
                
                os.system('aws ec2 delete-key-pair --key-name {}'.format(key_name))
            
            #elif cmd2=='15': # Stop Ec2 Instance
            elif ch2=='stop instance':
                print('Enter Instance id to stop Ec2 instances :-  ', end='')
                id=input()
                os.system('aws ec2 stop-instances --instance-ids {}'.format(id))
            
            elif ch2=='start instance':
                print('Enter Instance id to start Ec2 instances :-  ', end='')
                id=input()
                os.system('aws ec2 start-instances --instance-ids {}'.format(id))
            
            elif ch2=='terminate instance' or ch2=='delete instance':
                print('Enter Instance id to terminate Ec2 instances :-  ', end='')
                id=input()
                os.system('aws ec2 terminate-instances --instance-ids {}'.format(id))
            
            elif ch2=='delete security group':
                sg_id=input('Enter Security group id you want to delete :-  ')
                os.system('aws ec2 delete-security-group --group-id {}'.format(sg_id))
            
            elif ch2=='go back to previous menu' or ch2=='go back' or ch2=='0':
                p.speak('going back to previous menu')
                break
            else:
                print('Please enter valid command')

    elif option=='start namenode' or option=='conifgure name node':
        p.speak('Enter IP Address')
        remote_ip=input('IP Address :-    ')
       
        os.system('ssh root@{} hadoop-daemon.sh start namenode'.format(remote_ip))
        os.system('ssh root@{} jps'.format(remote_ip))
        os.system('ssh root@{} hadoop dfsadmin -report'.format(remote_ip))
        p.speak('NameNode Starts')


    elif option=='start data node' or option=='start datanode':
        p.speak('Enter IP Address')
        remote_ip=input('IP Address :-    ')
        os.system('ssh root@{} hadoop-daemon.sh start datanode'.format(remote_ip))
        os.system('ssh root@{} jps'.format(remote_ip))
        os.system('ssh root@{} hadoop dfsadmin -report'.format(remote_ip))
        p.speak('Datanode starts')
        p.speak('Hadoop Cluster Created')

    
    elif option=='configure web server' or option=='configure webserver':
        p.speak('Enter IP Address')
        remote_ip=input('IP Address :-    ')
        os.system('ssh root@{} sudo yum install httpd -y'.format(remote_ip))
        os.system('ssh root@{} sudo systemctl start httpd'.format(remote_ip))
        os.system('ssh root@{} sudo systemctl enable httpd'.format(remote_ip))
        os.system('scp index.html root@{}:/var/www/html'.format(remote_ip))
        p.speak('Webserver configured')

    elif option=='create logical volume' or option=='create lvm':
        p.speak('Enter IP Address')
        remote_ip=input('IP Address :-    ')
        p.speak('Tell Partition Size')
        partition_size=input('Partition Size :-  ')
        p.speak('Enter LV Name to assign to partition')
        lv_name = input('LV Name to assign to partition :-  ')
        p.speak('Enter Virtual Group Name to create partition')
        vg_name = input('Virtual Group Name to create partition :- ')
        os.system('ssh root@{} sudo lvcreate --size {}G --name {} {}'.format(remote_ip , partition_size , lv_name , vg_name))
        os.system('ssh root@{} sudo mkfs.ext4 /dev/{}/{}'.format(remote_ip , vg_name , lv_name))
        p.speak('Enter directory name to mount Logical Volume')
        dir_name=input('directory name to mount Logical Volume :-  ')
        os.system('ssh root@{} sudo mkdir {}'.format(remote_ip , dir_name))
        os.system('ssh root@{} sudo mount /dev/{}/{} {}'.format(remote_ip , vg_name , lv_name , dir_name))
        os.system('ssh root@{} sudo df -h'.format(remote_ip))
        p.speak('logical volume created')

    elif option=='create vg' or option=='create virtual group' or option=='create v g':
        p.speak('Enter IP Address')
        remote_ip=input('IP Address :-   ')
        p.speak('Tell First Device name to create Logical Volume :-  ')
        device1=input('1st Device Name :-    ') 
        p.speak('Tell Second Device name to create Logical Volume :-  ')
        device2=input('Second device Name :-   ')
        os.system('ssh root@{} sudo pvcreate {}'.format(remote_ip , device1))
        os.system('ssh root@{} sudo pvcreate {}'.format(remote_ip , device2))

        p.speak('Please Enter name to create Virtual Group')
        vg_name=input('Enter name to create Virtual Group :-  ')
        os.system('ssh root@{} sudo vgcreate {} {} {}'.format(remote_ip , vg_name , device1 , device2))
        os.system('ssh root@{} sudo vgdisplay {}'.format(remote_ip , vg_name))
        p.speak('virtual group created')

    
    elif option=='configure docker' or option=='automate docker' or option=='automate docker container' or option=='2':

        print("enter remote OS IP :-   ", end='')
        remote_ip=input()

        while True:
            p.speak('Configuring  Docker  Container')
            print('\t\t\t\t\tpull image from docker hub')
            print('\t\t\t\t\tlaunch Container')
            print('\t\t\t\t\tknow number of docker container running in local OS')
            print('\t\t\t\t\tknow number of images in Local OS')
            print('\t\t\t\t\tInspect docker Container')
            print('\t\t\t\t\tStop docker container')
            print('\t\t\t\t\tStart docker container')
            print('\t\t\t\t\tremove image from local OS')
            print('\t\t\t\t\tdelete Single docker container')
            print('\t\t\t\t\tdelete all docker container')
            print('\t\t\t\t\tConfigure webserver inside docker container')
            print()
            
            with sr.Microphone() as source:
                print('Tell me what you truely desire')
                audio=r.listen(source)
            
            ch=r.recognize_google(audio)
            ch=ch.lower()
            print(ch)

         #   p.speak('Tell me what you truely desire')
         #   ch=input('Enter what you want to do  :-  ')
            #if cmd2=='1': #Pull Image
            if ch=='pull image' or ch=='full image' or ch=='1':
                p.speak('pull image form docker hub')
                p.speak('Enter Image name to pull it from docker hub')
                value=input('Image name to pull it from docker hub :-  ')
                os.system("ssh root@{} sudo docker pull {}".format(remote_ip , value))
                p.speak('Image pulled from docker hub')            
            #elif cmd2=='2': # Launch Container
            elif ch=='launch container' or ch=='2':
                p.speak('Launching docker container')
                p.speak('Enter Container name to launch it')
                value=input('Container Name :-   ')
                p.speak('enter image name to launch container')
                image=input('Image Name :-   ')
                os.system("ssh root@{} sudo docker run -dit --name {} {}".format(remote_ip , value, image))
                os.system('ssh root@{} sudo docker ps'.format(remote_ip))
                p.speak('container launched')
            #elif cmd2=='3': # No of Container running
            elif ch=='number of container running' or ch=='container running' or ch=='tell me how many container running' or ch=='3':
                p.speak('number of docker container running')
                os.system('ssh root@{} sudo docker ps'.format(remote_ip))
            
            #elif cmd2=='4': # No of Docker Images in OS
            elif ch=='tell me number of docker images' or ch=='tell me number of docker image' or ch=='number of docker image' or ch=='4':
                p.speak('Number of docker images ')
                os.system('ssh root@{} sudo docker images'.format(remote_ip))
            
            #elif cmd2=='5': 
            elif ch=='inspect docker' or ch=='5':
                p.speak('Tell container name to inspect')
                value=input('container name to Inspect :-   ')
                os.system('ssh root@{} docker inspect {}'.format(remote_ip , value))

            elif ch=='go back' or ch=='back to previous menu':
                break
            #elif cmd2=='6':
            elif ch=='stop container':
                with sr.Microphone() as source:
                    print('Tell me container name to Stop')
                    audio=r.listen(source)
                value=r.recognize_google(source)
                value=value.lower()
                print(value)

                os.system('ssh root@{} docker stop {}'.format(remote_ip , value))
                
            
            #elif cmd2=='7':
            elif ch=='start container':
                with sr.Microphone() as source:
                    print('Tell me container name to Start')
                    audio=r.listen(source)
                value=r.recognize_google(source)
                value=value.lower()
                print(value)

                os.system('ssh root@{} docker start {}'.format(remote_ip , value))
                
            #elif cmd2=='8':
            elif ch=='remove image':
                with sr.Microphone() as source:
                    print('Tell me Image name to delete')
                    audio=r.listen(source)
                value=r.recognize_google(source)
                value=value.lower()
                print(value)

                os.system('ssh root@{} docker rmi {}'.format(remote_ip , value))
            
            #elif cmd2=='9':
            elif ch=='remove single container' or ch=='delete single container':
                with sr.Microphone() as source:
                    print('Tell me container name to delete')
                    audio=r.listen(source)
                value=r.recognize_google(source)
                value=value.lower()
                print(value)

                os.system('ssh root@{} docker rm -f {}'.format(remote_ip , value))
            
            #elif cmd2=='10':
            elif ch=='remove all container' or ch=='delete all container':
                os.system('ssh root@{} sudo docker rm -f $(sudo docker ps  -a -q)'.format(remote_ip))
            
            #elif cmd2=='11':
            elif ch=='configure web server inside docker':
                with sr.Microphone() as source:
                    print("tell container name")
                    audio=r.listen(source)
                con_name=r.recognize_google(audio)
                con_name=con_name.lower()
                print(con_name)
                with sr.Microphone() as source:
                    print("tell image name")
                    audio=r.listen(source)
                image_name=r.recognize_google(audio)
                image_name=image_name.lower()
                print(image_name)

                with sr.Microphone() as source:
                    print('tell Port Number to Expose the WebServer running on the top of Docker :-  ')
                    audio=r.listen(source)
                port=r.recognize_google(audio)
                print(port)

                os.system('ssh root@{} sudo docker run -dit --name {} -p {}:80 {}'.format(remote_ip , con_name , port , image_name))
                os.system('ssh root@{} sudo docker exec -it {} yum install httpd -y'.format(remote_ip , con_name))
                os.system('ssh root@{} sudo docker cp /automation/index.html {}:/var/www/html/'.format(remote_ip , con_name))
                os.system('ssh root@{} sudo docker exec -it {} /usr/sbin/httpd'.format(remote_ip , con_name))
                os.system('ssh root@{} sudo docker ps'.format(remote_ip))
            #elif cmd2=='12':
            

    elif option=='add more hard disk to vg' or option=='add extra hard disks to vg' or option=='add extra hard disk to vg':
        remote_ip=input('Enter IP Address :-    ')
        print('Please Enter Device Name to attach to the Virtual Group :-  ', end='')
        device_name=input()
        os.system('ssh root@{} sudo pvcreate {}'.format(remote_ip , device_name))
        print('Please Enter Virtual Group Name to extend its size :-  ', end='')
        vg_name=input()
        os.system('ssh root@{} sudo vgextend {} {}'.format(remote_ip , vg_name , device_name))
        os.system('ssh root@{} sudo vgdisplay {}'.format(remote_ip , vg_name))

    elif option=='increase lvm size' or option=='increase LVM size':
        remote_ip=input('Enter IP Address :-    ')    
        with sr.Microphone() as source:
            print('Tell size to increase the Logical Volume Size online :-  ')
            audio=r.listen(source)
        size=r.recognize_google(audio)
        print('Please Enter Virtual Group Name to extend its size :-  ', end='')
        vg_name=input()
        print('Please Enter Logical Volume Name to extend its size :-  ', end='')
        lv_name=input()
        os.system('ssh root@{} sudo lvextend --size +{}G /dev/{}/{}'.format(remote_ip , size , vg_name , lv_name))
        os.system('ssh root@{} sudo resize2fs /dev/{}/{}'.format(remote_ip , vg_name , lv_name ))
        os.system('ssh root@{} sudo df -h'.format(remote_ip))
    
    elif option=='prediction automation' or option=='predict future value' or option=='automation prediction':
        os.system('python salary.py')

    elif option=='exit' or option=='go back' or option=='stop' or option=='0':
        break
    else:
        print('\n\t\t\t\t\t\t\tPlease Choose Valid Options mention above')
