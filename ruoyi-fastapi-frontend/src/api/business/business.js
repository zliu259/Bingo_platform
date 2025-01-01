import request from '@/utils/request'

// project api
export function getProjectList() {
  return request({
    url: '/business/projects',
    method: 'get',
  })
}