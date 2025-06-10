FROM nginx:latest

# Copy custom configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy static files
COPY static /usr/share/nginx/html

# Expose port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]