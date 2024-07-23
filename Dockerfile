#httpd is the official Apache HTTP server image from Docker Hub.
FROM httpd
#This command updates the package lists for the APT package manager. The -y flag automatically answers "yes" to any prompts, allowing the command to run non-interactively
RUN apt-get update -y 
#This installs Git on the container. Again, the -y flag allows the installation to proceed without user interaction.
RUN apt-get install git -y 
#This clones a Git repository from GitHub into the container. The repository contains the files for the custom website
RUN git clone https://github.com/nandakumar08/my-website.git
#This command removes the default index.html file from the Apache document root directory
RUN rm -rf /usr/local/apache2/htdocs/index.html
#This moves the cloned website files from their current location to the Apache document root directory (/usr/local/apache2/htdocs), making them accessible to the web server
RUN mv /usr/local/apache2/my-website /usr/local/apache2/htdocs
#
RUN docker run -itd --name Nandakumar --p 555:80 my-website
