// Function to check if the user has upvoted the post
async function checkUpvote() {
  const id = window.location.toString().split('/')[
      window.location.toString().split('/').length - 1
  ];

  try {
      const response = await fetch(`/api/posts/${id}/has_upvoted`);
      if (response.ok) {
          const data = await response.json();
          return data.has_upvoted;
      } else {
          console.error('Failed to check upvote');
          return false;
      }
  } catch (error) {
      console.error('Error checking upvote:', error);
      return false;
  }
}

// Function to handle the click event on the like button
async function upvoteClickHandler(event) {
  event.preventDefault();

  const hasUpvoted = await checkUpvote();
  if (hasUpvoted) {
      alert('You have already upvoted this post.');
  } else {
      const id = window.location.toString().split('/')[
          window.location.toString().split('/').length - 1
      ];
      const response = await fetch('/api/posts/upvote', {
          method: 'PUT',
          body: JSON.stringify({
              post_id: id
          }),
          headers: {
              'Content-Type': 'application/json'
          }
      });

      if (response.ok) {
          document.location.reload();
      } else {
          const responseData = await response.json();
          alert(responseData.message);
      }
  }
}

document.querySelector('.like-post-btn').addEventListener('click', upvoteClickHandler);

// Check if the user has upvoted the post when the page loads
document.addEventListener('DOMContentLoaded', async () => {
  const hasUpvoted = await checkUpvote();
  if (hasUpvoted) {
      // Disable the like button if the user has already upvoted the post
      document.querySelector('.like-post-btn').disabled = true;
  }
});
