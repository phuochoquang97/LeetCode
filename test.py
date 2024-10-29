def process_candidates(top_N_idx):
    """
    Calculate the inlier scores between query and it matches
    - Input: index of top matches
    - Output: the inlier scores of each match
    """
    inlier_scores = []

    for candidate_idx in top_N_idx:
        # get frames and descriptors for the candidate image
        candidate_url = imdb_url(candidate_idx)
        candidate = imread(candidate_url, pilmode="RGB")
        [candidate_frames, candidate_descrs] = cyvlfeat.sift.sift(
            rgb2gray(candidate), peak_thresh=0.01, float_descriptors=True
        )

        # find matches between query and candidate
        matches = matching(frames, candidate_frames, descrs, candidate_descrs)

        # filter with RANSAC
        tnf, inliers = ransac(frames, candidate_frames, matches)

        if inliers is not None:
            inlier_scores.append((candidate_idx, len(inliers)))

    return inlier_scores
